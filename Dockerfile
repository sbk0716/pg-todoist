# python3.9のイメージをダウンロード
FROM python:3.9-buster

# If given, Python won’t try to write .pyc files on the import of source modules.
ENV PYTHONDONTWRITEBYTECODE 1

# Force the stdout and stderr streams to be unbuffered. This option has no effect on the stdin stream.
ENV PYTHONUNBUFFERED 1

WORKDIR /src

# Install poetry/psycopg2/starlette using pip.
RUN pip install poetry psycopg2 starlette

# poetryの定義ファイルをコピー (存在する場合)
COPY pyproject.toml* poetry.lock* ./

# poetryでライブラリをインストール (pyproject.tomlが既にある場合)
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install; fi

# uvicornのサーバーを立ち上げる
ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]