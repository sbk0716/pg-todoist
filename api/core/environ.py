from starlette.config import Config
from starlette.datastructures import Secret
from databases import DatabaseURL
import os

config = Config(".env")

PROJECT_NAME = "ToDoIst API"
DESCRIPTION = "RESTful API for ToDoIst App"
VERSION = "1.0.0"
API_PREFIX = "/api"

POSTGRES_USER = config("POSTGRES_USER", cast=str, default="admin")
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret)
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="app-db")
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")

if os.environ.get("ENV") and os.environ.get("ENV") == "test":
    # test db
    POSTGRES_DB = "testdb"
else:
    POSTGRES_DB = config("POSTGRES_DB", cast=str, default="coredb")

DB_URL_STR = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

DB_URL = config("DB_URL", cast=DatabaseURL, default=f"{DB_URL_STR}")
