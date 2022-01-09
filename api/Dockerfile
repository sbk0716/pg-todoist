# Set the baseImage to use for subsequent instructions.
FROM python:3.9-buster

# If given, Python won’t try to write .pyc files on the import of source modules.
ENV PYTHONDONTWRITEBYTECODE 1

# Force the stdout and stderr streams to be unbuffered. This option has no effect on the stdin stream.
ENV PYTHONUNBUFFERED 1

# Set the working directory.
WORKDIR /src

# Copy all files.
COPY ./ ./

# List files and directories.
RUN ls -la && sleep 5

# Install poetry/psycopg2/starlette using pip.
RUN pip install poetry psycopg2 starlette

# If the poetry definition file exists, copy it to the dest path in the image's file system.
COPY pyproject.toml* poetry.lock* ./

# Create the virtualenv inside the project’s root directory.
RUN poetry config virtualenvs.in-project true

# If the poetry definition file exists, install the library using poetry.
RUN if [ -f pyproject.toml ]; then poetry install; fi

# Start the uvicorn server
ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]