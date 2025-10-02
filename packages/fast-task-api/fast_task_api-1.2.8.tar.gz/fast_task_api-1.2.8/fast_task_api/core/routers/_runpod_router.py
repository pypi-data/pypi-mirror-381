import functools
import inspect
import traceback
from datetime import datetime, timezone
from typing import Union, Callable

from fast_task_api.CONSTS import SERVER_HEALTH
from fast_task_api.core.job.base_job import JOB_STATUS
from fast_task_api.core.job.job_progress import JobProgressRunpod, JobProgress
from fast_task_api.core.job.job_result import JobResultFactory, JobResult
from fast_task_api.core.routers._socaity_router import _SocaityRouter
from fast_task_api.core.routers.router_mixins._base_file_handling_mixin import _BaseFileHandlingMixin

from fast_task_api.CONSTS import FTAPI_DEPLOYMENTS
from fast_task_api.core.utils import normalize_name
from fast_task_api.settings import FTAPI_DEPLOYMENT, FTAPI_PORT, DEFAULT_DATE_TIME_FORMAT


class SocaityRunpodRouter(_SocaityRouter, _BaseFileHandlingMixin):
    """
    Adds routing functionality for the runpod serverless framework.
    Provides enhanced file handling and conversion capabilities.
    """
    def __init__(self, title: str = "FastTaskAPI for ", summary: str = None, *args, **kwargs):
        super().__init__(title=title, summary=summary, *args, **kwargs)
        self.routes = {}  # routes are organized like {"ROUTE_NAME": "ROUTE_FUNCTION"}

        self.add_standard_routes()

    def add_standard_routes(self):
        self.task_endpoint(path="openapi.json")(self.get_openapi_schema)

    def task_endpoint(
            self,
            path: str = None,
            *args,
            **kwargs
    ):
        """
        Adds an additional wrapper to the API path to add functionality like:
        - Add api key validation
        - Create a job and add to the job queue
        - Return job
        """
        path = normalize_name(path, preserve_paths=True)
        if len(path) > 0 and path[0] == "/":
            path = path[1:]

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*wrapped_func_args, **wrapped_func_kwargs):
                self.status = SERVER_HEALTH.BUSY
                ret = func(*wrapped_func_args, **wrapped_func_kwargs)
                self.server_status = SERVER_HEALTH.RUNNING
                return ret

            self.routes[path] = wrapper
            return wrapper

        return decorator

    def get(self, path: str = None, queue_size: int = 1, *args, **kwargs):
        return self.task_endpoint(path=path, queue_size=queue_size, *args, **kwargs)

    def post(self, path: str = None, queue_size: int = 1, *args, **kwargs):
        return self.task_endpoint(path=path, queue_size=queue_size, *args, **kwargs)

    def endpoint(self, path: str = None, *args, **kwargs):
        return self.task_endpoint(path=path, *args, **kwargs)

    def _add_job_progress_to_kwargs(self, func, job, kwargs):
        """
        Add job_progress parameter to function arguments if necessary.

        Args:
            func: Original function
            job: Runpod job
            kwargs: Current function arguments

        Returns:
            Updated kwargs with job_progress added
        """
        job_progress_params = []
        for param in inspect.signature(func).parameters.values():
            if param.annotation in (JobProgress, JobProgressRunpod) or param.name == "job_progress":
                job_progress_params.append(param.name)

        if job_progress_params:
            jp = JobProgressRunpod(job)
            for job_progress_param in job_progress_params:
                kwargs[job_progress_param] = jp

        return kwargs

    def _router(self, path, job, **kwargs):
        """
        Internal app function that routes the path to the correct function.

        Args:
            path: Route path
            job: Runpod job
            kwargs: Function arguments

        Returns:
            JSON-encoded job result
        """
        if not isinstance(path, str):
            raise Exception("Path must be a string")

        path = normalize_name(path, preserve_paths=True)
        path = path.strip("/")

        route_function = self.routes.get(path, None)
        if route_function is None:
            raise Exception(f"Route {path} not found")

        # Add job progress to kwargs if necessary
        kwargs = self._add_job_progress_to_kwargs(route_function, job, kwargs)

        # Check for missing arguments
        sig = inspect.signature(route_function)
        missing_args = [arg for arg in sig.parameters if arg not in kwargs]
        if missing_args:
            raise Exception(f"Arguments {missing_args} are missing")

        # Handle file uploads and conversions
        route_function = self._handle_file_uploads(route_function)

        # Prepare result tracking
        start_time = datetime.now(timezone.utc)
        # result = JobResultFactory.from_base_job(job)
        result = JobResult(id=job['id'], execution_started_at=start_time.strftime("%Y-%m-%dT%H:%M:%S.%f%z"))

        try:
            # Execute the function
            res = route_function(**kwargs)

            # Convert result to JSON if it's a MediaFile / MediaList
            res = JobResultFactory._serialize_result(res)

            result.result = res
            result.status = JOB_STATUS.FINISHED.value
        except Exception as e:
            result.error = str(e)
            result.status = JOB_STATUS.FAILED.value
            print(f"Job {job['id']} failed: {str(e)}")
            traceback.print_exc()
        finally:
            result.execution_finished_at = datetime.now(timezone.utc).strftime(DEFAULT_DATE_TIME_FORMAT)

        result = result.model_dump_json()
        return result

    def handler(self, job):
        """
        The handler function that is called by the runpod serverless framework.
        We wrap it to provide internal routing in the serverless framework.
        Args:
            job: the job that is passed by the runpod serverless framework. Must include "path" in the input.
        Returns: the result of the path function.
        """
        inputs = job["input"]
        if "path" not in inputs:
            raise Exception("No path provided")

        route = inputs["path"]
        del inputs["path"]

        return self._router(route, job, **inputs)

    def start_runpod_serverless_localhost(self, port):
        # add the -rp_serve_api to the command line arguments to allow debugging
        import sys
        sys.argv.append("--rp_serve_api")
        sys.argv.extend(["--rp_api_port", str(port)])

        # overwrite runpod variables. Little hacky but runpod does not expose the variables in a nice way.
        import runpod.serverless
        from runpod.serverless.modules import rp_fastapi
        rp_fastapi.TITLE = self.title + " " + rp_fastapi.TITLE
        rp_fastapi.DESCRIPTION = self.summary + " " + rp_fastapi.DESCRIPTION
        desc = '''\
                        In input declare your path as route for the function. Other parameters follow in the input as usual.
                        The FastTaskAPI app will use the path argument to route to the correct function declared with 
                        @task_endpoint(path="your_path").
                        { "input": { "path": "your_path", "your_other_args": "your_other_args" } }
                    '''
        rp_fastapi.RUN_DESCRIPTION = desc + "\n" + rp_fastapi.RUN_DESCRIPTION

        # hack to print version also in runpod
        version = self.version

        class WorkerAPIWithModifiedInfo(rp_fastapi.WorkerAPI):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self._orig_openapi_func = self.rp_app.openapi
                self.rp_app.openapi = self.custom_openapi

            def custom_openapi(self):
                if not self.rp_app.openapi_schema:
                    self._orig_openapi_func()
                self.rp_app.openapi_schema["info"]["fast-task-api"] = version
                self.rp_app.openapi_schema["info"]["runpod"] = rp_fastapi.runpod_version
                return self.rp_app.openapi_schema

        rp_fastapi.WorkerAPI = WorkerAPIWithModifiedInfo

        runpod.serverless.start({"handler": self.handler})

    def _create_openapi_compatible_function(self, func: Callable) -> Callable:
        """
        Create a function compatible with FastAPI OpenAPI generation by applying 
        the same conversion logic as the FastAPI mixin, but without runtime dependencies.

        This generates the rich schema with proper file upload handling.

        Args:
            func: Original function to convert
            max_upload_file_size_mb: Maximum file size in MB

        Returns:
            Function with FastAPI-compatible signature for OpenAPI generation
        """
        # Import FastAPI-specific conversion logic
        from fast_task_api.core.routers.router_mixins._fast_api_file_handling_mixin import _fast_api_file_handling_mixin
        from fast_task_api.core.job.job_result import JobResult
        import inspect
        from fast_task_api.core.utils import replace_func_signature
        # Create a temporary instance of the FastAPI mixin to use its conversion methods
        temp_mixin = _fast_api_file_handling_mixin(max_upload_file_size_mb=5)
        # Apply the same preparation logic as FastAPI router
        with_file_upload_signature = temp_mixin._prepare_func_for_media_file_upload_with_fastapi(func, 5)
        # 4. Set proper return type for job-based endpoints

        sig = inspect.signature(with_file_upload_signature)
        job_result_sig = sig.replace(return_annotation=JobResult)
        # Update the signature

        final_func = replace_func_signature(with_file_upload_signature, job_result_sig)
        return final_func

    def get_openapi_schema(self):
        from fastapi.openapi.utils import get_openapi
        from fastapi.routing import APIRoute

        fastapi_routes = []
        for path, func in self.routes.items():
            # Create FastAPI-compatible function for rich OpenAPI generation
            try:
                compatible_func = self._create_openapi_compatible_function(func)
                fastapi_routes.append(APIRoute(
                    path=f"/{path.strip('/')}", 
                    endpoint=compatible_func, 
                    methods=["POST"]
                ))
            except Exception as e:
                print(f"Error creating OpenAPI compatible function for {path}: {e}")
                # Fallback to safe function approach
                try:
                    safe_func = self._create_openapi_safe_function(func)
                    fastapi_routes.append(APIRoute(
                        path=f"/{path.strip('/')}",
                        endpoint=safe_func,
                        methods=["POST"],
                        response_model=None
                    ))
                except Exception as e2:
                    print(f"Error creating safe function for {path}: {e2}")
                    # Ultimate fallback - create minimal route

                    def minimal_func():
                        return {"message": "Documentation not available"}

                    fastapi_routes.append(APIRoute(
                        path=f"/{path.strip('/')}",
                        endpoint=minimal_func,
                        methods=["POST"],
                        response_model=None
                    ))

        # Generate the OpenAPI schema dict (similar to FastAPI openapi())
        schema = get_openapi(
            title=self.title,
            version="1.0.0",
            routes=fastapi_routes,
            summary=self.summary,
            description=self.summary,
        )

        # Add FastTaskAPI version information like the FastAPI router
        schema["info"]["fast-task-api"] = self.version

        return schema

    def start(self, deployment: Union[FTAPI_DEPLOYMENTS, str] = FTAPI_DEPLOYMENT, port: int = FTAPI_PORT, *args, **kwargs):
        if type(deployment) is str:
            deployment = FTAPI_DEPLOYMENTS(deployment)

        if deployment == deployment.LOCALHOST:
            self.start_runpod_serverless_localhost(port=port)
        elif deployment == deployment.SERVERLESS:
            import runpod.serverless
            runpod.serverless.start({"handler": self.handler})
        else:
            raise Exception(f"Not implemented for environment {deployment}")
