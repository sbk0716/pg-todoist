import MySQLdb
from starlette.config import Config

# Config will be read from environment variables and/or ".env" files.
config = Config(".env")
MYSQL_ROOT_USER = "root"
MYSQL_ROOT_PASSWORD = config("MYSQL_ROOT_PASSWORD", cast=str)
MYSQL_USER = config("MYSQL_USER", cast=str, default="admin")
MYSQL_PASSWORD = config("MYSQL_PASSWORD", cast=str)
MYSQL_HOST = config("MYSQL_HOST", cast=str, default="app-db")
MYSQL_TCP_PORT = config("MYSQL_TCP_PORT", cast=str, default="3306")
MYSQL_DATABASE = "testdb"

# Connect to database.
connection = MySQLdb.connect(
    host=MYSQL_HOST,
    user=MYSQL_ROOT_USER,
    passwd=MYSQL_ROOT_PASSWORD,
    db="mysql",
    charset="utf8",
)
# Generate cursor.
cursor = connection.cursor()

# CREATE DATABASE
create_db = f"CREATE DATABASE IF NOT EXISTS {MYSQL_DATABASE}"
cursor.execute(create_db)

# GRANT ALL
grant_all = f"GRANT ALL ON *.* TO '{MYSQL_USER}'@'%'"
cursor.execute(grant_all)

# ALTER USER
alter_user = f"ALTER USER '{MYSQL_USER}'@'%' IDENTIFIED WITH mysql_native_password BY '{MYSQL_PASSWORD}'"
cursor.execute(alter_user)

# SHOW DATABASE
show_db = "SHOW DATABASES"
cursor.execute(show_db)
rows = cursor.fetchall()
print("==================================================")
print("1. SHOW DATABASES")
print("==================================================")
for row in rows:
    print(row[0])
print("==================================================")

# SELECT USER
select_user = "SELECT user, host, plugin FROM mysql.user"
cursor.execute(select_user)
rows = cursor.fetchall()
print("==================================================")
print("2. SELECT user, host, plugin FROM mysql.user")
print("==================================================")
for row in rows:
    print(row)
print("==================================================")

connection.commit()
connection.close()
