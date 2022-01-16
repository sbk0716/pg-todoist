# Import logging | Logging package for Python.
import logging

# Set the logging level of this logger for uvicorn.
logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)
