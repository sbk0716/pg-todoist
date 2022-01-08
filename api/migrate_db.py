from sqlalchemy import create_engine

from api.models.task import Base

from api import environ

# Define DB_URL
DB_URL = environ.DB_URL
MYSQL_DATABASE = environ.MYSQL_DATABASE
print(f"MYSQL_DATABASE: {MYSQL_DATABASE}")
# DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"

engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()