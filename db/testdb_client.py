import psycopg2
from starlette.config import Config

config = Config(".env")
DEFAULT_POSTGRES_DB = "postgres"
POSTGRES_USER = config("POSTGRES_USER", cast=str, default="admin")
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=str)
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="app-db")
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
DB_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{DEFAULT_POSTGRES_DB}"
TEST_DB = "testdb"


def drop_all(connection):
    # Generate cursor.
    cursor = connection.cursor()

    # DROP DATABASE
    drop_db = f"DROP DATABASE {TEST_DB}"
    cursor.execute(drop_db)

    # DROP ROLE
    drop_role = f"DROP ROLE root"
    cursor.execute(drop_role)

    cursor.close()


def create_all(connection):
    # Generate cursor.
    cursor = connection.cursor()

    # CREATE DATABASE
    create_db = f"CREATE DATABASE {TEST_DB}"
    cursor.execute(create_db)

    # CREATE ROLE
    create_role = f"CREATE ROLE root LOGIN SUPERUSER PASSWORD '{POSTGRES_PASSWORD}'"
    cursor.execute(create_role)

    # SHOW DATABASES
    cursor.execute("SELECT datname, datdba, encoding, datcollate, datctype from pg_database;")
    rows = cursor.fetchall()
    print("==================================================")
    print("1. SELECT datname, datdba, encoding, datcollate, datctype from pg_database")
    print("==================================================")
    for row in rows:
        print(row)
    print("==================================================")

    # SHOW DATABASES
    cursor.execute("SELECT * FROM pg_user;")
    rows = cursor.fetchall()
    print("==================================================")
    print("2. SELECT * FROM pg_user")
    print("==================================================")
    for row in rows:
        print(row)
    print("==================================================")

    cursor.close()


if __name__ == "__main__":
    # Connect to database.
    connection = psycopg2.connect(DB_URL)
    connection.autocommit = True
    # Execute drop_all function.
    drop_all(connection)
    # Execute create_all function.
    create_all(connection)
    # Close connection.
    connection.close()
