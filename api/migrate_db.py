from sqlalchemy import create_engine

from api.models.task import Base

from api.core import environ

# Define DB_URL
DB_URL = environ.DB_URL
POSTGRES_DB = environ.POSTGRES_DB
print(f"POSTGRES_DB: {POSTGRES_DB}")
# DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"

engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()