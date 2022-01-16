from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from api.core import environ
from api.domain.models.task import Base

DB_URL_STR = environ.DB_URL_STR
POSTGRES_DB = environ.POSTGRES_DB
print(f"POSTGRES_DB: {POSTGRES_DB}")

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# target_metadata = None
# ========================================
# Set target_metadata
# ========================================
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

# ========================================
# Set sqlalchemy.url
# ========================================
# set_main_option: Set an option programmatically within the ‘main’ section.
# sqlalchemy.url - A URL to connect to the database via SQLAlchemy.
# https://alembic.sqlalchemy.org/en/latest/api/config.html?highlight=set_main_option#alembic.config.Config.set_main_option
config.set_main_option("sqlalchemy.url", str(DB_URL_STR))


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    # Indicates type comparison behavior during an autogenerate operation.
    # Set to True to turn on default type comparison.
    # https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.compare_type
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    # Indicates type comparison behavior during an autogenerate operation.
    # Set to True to turn on default type comparison.
    # https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.compare_type
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    print("execute run_migrations_offline")
    run_migrations_offline()
else:
    print("execute run_migrations_online")
    run_migrations_online()
