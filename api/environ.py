# Starlette is a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services.
# https://www.starlette.io/config/
from starlette.config import Config

# https://www.starlette.io/config/#secrets
from starlette.datastructures import Secret
import os

# Config will be read from environment variables and/or ".env" files.
config = Config(".env")

PROJECT_NAME = "ToDoIst API"
DESCRIPTION = "RESTful API for ToDoIst App"
VERSION = "1.0.0"
API_PREFIX = "/api"

# SECRET_KEY = config("SECRET_KEY", cast=Secret, default="CHANGEME")
MYSQL_ROOT_USER = "root"
MYSQL_ROOT_PASSWORD = config("MYSQL_ROOT_PASSWORD", cast=Secret)
MYSQL_USER = config("MYSQL_USER", cast=str, default="admin")
MYSQL_PASSWORD = config("MYSQL_PASSWORD", cast=Secret)
MYSQL_HOST = config("MYSQL_HOST", cast=str, default="app-db")
MYSQL_TCP_PORT = config("MYSQL_TCP_PORT", cast=str, default="3306")

if os.environ.get("ENV") and os.environ.get("ENV") == "test":
    # test db
    MYSQL_DATABASE = "testdb"
else:
    MYSQL_DATABASE = config("MYSQL_DATABASE", cast=str, default="coredb")

# https://docs.sqlalchemy.org/en/14/dialects/mysql.html#aiomysql
ASYNC_DB_URL = f"mysql+aiomysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_TCP_PORT}/{MYSQL_DATABASE}"
# https://docs.sqlalchemy.org/en/14/dialects/mysql.html#module-sqlalchemy.dialects.mysql.pymysql
DB_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_TCP_PORT}/{MYSQL_DATABASE}"
