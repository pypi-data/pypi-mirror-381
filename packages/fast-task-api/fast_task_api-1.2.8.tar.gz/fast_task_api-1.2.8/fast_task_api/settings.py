import sys
from os import environ
from fast_task_api.CONSTS import FTAPI_BACKENDS, FTAPI_DEPLOYMENTS

# Set the execution mode
FTAPI_DEPLOYMENT = environ.get("FTAPI_DEPLOYMENT", FTAPI_DEPLOYMENTS.LOCALHOST)
FTAPI_BACKEND = environ.get("FTAPI_BACKEND", FTAPI_BACKENDS.FASTAPI)
# Configure the host and port
FTAPI_HOST = environ.get("FTAPI_HOST", "0.0.0.0")
FTAPI_PORT = int(environ.get("FTAPI_PORT", 8000))
# Server domain. Is used to build the refresh and cancel job urls. 
# If not set will just be /status?job_id=...
# Set it will be server_domain/status?job_id=...
SERVER_DOMAIN = environ.get("SERVER_DOMAIN", "")

# For example the datetime in the job response is formatted to and from this format
DEFAULT_DATE_TIME_FORMAT = environ.get("FTAPI_DATETIME_FORMAT", '%Y-%m-%dT%H:%M:%S.%f%z')

# to run the runpod serverless framework locally, the following two lines must be added
if FTAPI_BACKEND == FTAPI_BACKENDS.RUNPOD and FTAPI_DEPLOYMENT == FTAPI_DEPLOYMENTS.LOCALHOST:
    sys.argv.extend(['rp_serve_api', '1'])
    sys.argv.extend(['--rp_serve_api', '1'])
