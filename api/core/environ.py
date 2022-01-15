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

DB_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

# DB_URL = config(
#     "DB_URL",
#     cast=DatabaseURL,
#     default=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
# )

# # https://docs.sqlalchemy.org/en/14/dialects/mysql.html#aiomysql
# ASYNC_DB_URL = f"mysql+aiomysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_TCP_PORT}/{POSTGRES_DB}"
# # https://docs.sqlalchemy.org/en/14/dialects/mysql.html#module-sqlalchemy.dialects.mysql.pymysql
# DB_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_TCP_PORT}/{POSTGRES_DB}"

# ASYNC_DB_URL = config(
#     "ASYNC_DB_URL",
#     cast=DatabaseURL,
#     default=f"mysql+aiomysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_TCP_PORT}/{POSTGRES_DB}"
# )
# DB_URL = config(
#     "DB_URL",
#     cast=DatabaseURL,
#     default=f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_TCP_PORT}/{POSTGRES_DB}"
# )
