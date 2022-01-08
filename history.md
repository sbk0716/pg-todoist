# 確認
```sh
admin@gw-mac fast-todo % docker-compose version
docker-compose version 1.29.2, build 5becea4c
docker-py version: 5.0.0
CPython version: 3.9.0
OpenSSL version: OpenSSL 1.1.1h  22 Sep 2020
admin@gw-mac fast-todo % 
```

# docker-compose関連ファイルの作成
```sh
admin@gw-mac fast-todo % touch docker-compose.yaml
admin@gw-mac fast-todo % touch Dockerfile
```

# イメージのビルド
```sh
admin@gw-mac fast-todo % docker images
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
admin@gw-mac fast-todo % 
admin@gw-mac fast-todo % docker-compose build
Building demo-app
[+] Building 1.0s (11/11) FINISHED                                             
 => [internal] load build definition from Dockerfile                      0.0s
...
...
 => => naming to docker.io/library/fast-todo_demo-app                     0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
admin@gw-mac fast-todo % 
admin@gw-mac fast-todo % docker images
REPOSITORY           TAG       IMAGE ID       CREATED          SIZE
fast-todo_demo-app   latest    bf5ba6403fd9   10 seconds ago   882MB
admin@gw-mac fast-todo % 
```

# poetryによるPython環境のセットアップ
```sh
admin@gw-mac fast-todo % docker-compose run \
  --entrypoint "poetry init \
    --name demo-app \
    --dependency fastapi \
    --dependency uvicorn[standard]" \
  demo-app
Creating network "fast-todo_default" with the default driver
Creating fast-todo_demo-app_run ... done

This command will guide you through creating your pyproject.toml config.

Version [0.1.0]:  
Description []:  
Author [None, n to skip]:  n
License []:  
Compatible Python versions [^3.9]:  

Using version ^0.70.0 for fastapi
Using version ^0.16.0 for uvicorn
Would you like to define your main dependencies interactively? (yes/no) [yes] 
You can specify a package in the following forms:
  - A single name (requests)
  - A name and a constraint (requests@^2.23.0)
  - A git url (git+https://github.com/python-poetry/poetry.git)
  - A git url with a revision (git+https://github.com/python-poetry/poetry.git#develop)
  - A file path (../my-package/my-package.whl)
  - A directory (../my-package/)
  - A url (https://example.com/packages/my-package-0.1.0.tar.gz)

Search for package to add (or leave blank to continue): 

Would you like to define your development dependencies interactively? (yes/no) [yes] 
Search for package to add (or leave blank to continue): 

Generated file

[tool.poetry]
name = "demo-app"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.9"
fastapi = "^0.70.0"
uvicorn = {extras = ["standard"], version = "^0.16.0"}

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes] 
admin@gw-mac fast-todo % 
admin@gw-mac fast-todo % ls -la | grep toml
-rw-r--r--   1 admin  staff   352 Dec 10 19:49 pyproject.toml
admin@gw-mac fast-todo % 
```

# FastAPIのインストール
```sh
admin@gw-mac fast-todo % docker-compose run --entrypoint "poetry install" demo-app
Creating fast-todo_demo-app_run ... done
The virtual environment found in /src/.venv seems to be broken.
Recreating virtualenv demo-app in /src/.venv
Updating dependencies
Resolving dependencies... (11.7s)

Writing lock file

Package operations: 17 installs, 0 updates, 0 removals

  • Installing idna (3.3)
  • Installing sniffio (1.2.0)
  • Installing anyio (3.4.0)
  • Installing typing-extensions (4.0.1)
  • Installing asgiref (3.4.1)
  • Installing click (8.0.3)
  • Installing h11 (0.12.0)
  • Installing httptools (0.3.0)
  • Installing pydantic (1.8.2)
  • Installing python-dotenv (0.19.2)
  • Installing pyyaml (6.0)
  • Installing starlette (0.16.0)
  • Installing uvloop (0.16.0)
  • Installing watchgod (0.7)
  • Installing websockets (10.1)
  • Installing fastapi (0.70.0)
  • Installing uvicorn (0.16.0)
admin@gw-mac fast-todo % 
admin@gw-mac fast-todo % ls -la | grep lock
-rw-r--r--   1 admin  staff  33487 Dec 10 19:54 poetry.lock
admin@gw-mac fast-todo % 
admin@gw-mac fast-todo % docker-compose run --entrypoint "poetry install" demo-app
Creating fast-todo_demo-app_run ... done
Installing dependencies from lock file

No dependencies to install or update
admin@gw-mac fast-todo % 
admin@gw-mac fast-todo % docker-compose build --no-cache
Building demo-app
[+] Building 14.0s (11/11) FINISHED                                                  
...
...
Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
admin@gw-mac fast-todo % 
```


# Hello World!
```sh
admin@gw-mac fast-todo % mkdir api
admin@gw-mac fast-todo % touch api/__init__.py
admin@gw-mac fast-todo % touch api/main.py
admin@gw-mac fast-todo % 
admin@gw-mac fast-todo % tree -L 2
.
├── Dockerfile
├── README.md
├── api
│   ├── __init__.py
│   └── main.py
├── docker-compose.yaml
├── history.md
├── poetry.lock
└── pyproject.toml

1 directory, 8 files
admin@gw-mac fast-todo % 
admin@gw-mac fast-todo % docker-compose up  
Creating network "fast-todo_default" with the default driver
Creating fast-todo_demo-app_1 ... done
Attaching to fast-todo_demo-app_1
demo-app_1  | INFO:     Will watch for changes in these directories: ['/src']
demo-app_1  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
demo-app_1  | INFO:     Started reloader process [1] using watchgod
demo-app_1  | INFO:     Started server process [10]
demo-app_1  | INFO:     Waiting for application startup.
demo-app_1  | INFO:     Application startup complete.
demo-app_1  | INFO:     172.19.0.1:59556 - "GET /hello HTTP/1.1" 200 OK
^CGracefully stopping... (press Ctrl+C again to force)
Stopping fast-todo_demo-app_1 ... done
admin@gw-mac fast-todo % 
```

# ディレクトリ構造について
```sh
admin@gw-mac fast-todo % cd api                            
admin@gw-mac api % mkdir schemas routers models cruds
admin@gw-mac api % ls -l
total 8
-rw-r--r--  1 admin  staff    0 Dec 10 20:14 __init__.py
drwxr-xr-x@ 4 admin  staff  128 Dec 10 20:24 __pycache__
drwxr-xr-x@ 2 admin  staff   64 Dec 10 20:49 cruds
-rw-r--r--  1 admin  staff  123 Dec 10 20:14 main.py
drwxr-xr-x@ 2 admin  staff   64 Dec 10 20:49 models
drwxr-xr-x@ 2 admin  staff   64 Dec 10 20:49 routers
drwxr-xr-x@ 2 admin  staff   64 Dec 10 20:49 schemas
admin@gw-mac api % 
```

# パスオペレーション関数の作成
```sh
admin@gw-mac fast-todo % touch api/routers/task.py
admin@gw-mac fast-todo % touch api/routers/done.py
dmin@gw-mac fast-todo % docker-compose up 
Starting fast-todo_demo-app_1 ... done
Attaching to fast-todo_demo-app_1
demo-app_1  | INFO:     Will watch for changes in these directories: ['/src']
demo-app_1  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
demo-app_1  | INFO:     Started reloader process [1] using watchgod
demo-app_1  | INFO:     Started server process [11]
demo-app_1  | INFO:     Waiting for application startup.
demo-app_1  | INFO:     Application startup complete.
demo-app_1  | INFO:     172.19.0.1:59564 - "GET /docs HTTP/1.1" 200 OK
demo-app_1  | INFO:     172.19.0.1:59564 - "GET /openapi.json HTTP/1.1" 200 OK
demo-app_1  | INFO:     172.19.0.1:59562 - "PUT /tasks/%7Btask_id%7D HTTP/1.1" 200 OK
^CGracefully stopping... (press Ctrl+C again to force)
Stopping fast-todo_demo-app_1 ... done
admin@gw-mac fast-todo % 
```

# レスポンス型の定義
```sh
admin@gw-mac fast-todo % touch api/schemas/task.py
admin@gw-mac fast-todo % 
admin@gw-mac fast-todo % curl -X 'GET' \
  'http://localhost:8000/tasks' \
  -H 'accept: application/json'
[{"id":1,"title":"1つ目のTODOタスク","done":false}]%                           
admin@gw-mac fast-todo % 
```

# MySQLコンテナの立ち上げ
```sh
admin@gw-mac fast-todo % docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS          PORTS                                                    NAMES
07b4fa49482b   fast-todo_demo-app   "poetry run uvicorn …"   31 seconds ago   Up 29 seconds   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp                fast-todo_demo-app_1
abb4bf57d4b6   mysql:8.0            "docker-entrypoint.s…"   31 seconds ago   Up 30 seconds   33060/tcp, 0.0.0.0:33306->3306/tcp, :::33306->3306/tcp   fast-todo_db_1
admin@gw-mac fast-todo % 
admin@gw-mac fast-todo % docker-compose exec db mysql demo
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.27 MySQL Community Server - GPL

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| demo               |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

mysql> exit
Bye
admin@gw-mac fast-todo % 
```

# mysqlクライアントのインストール
```sh
admin@gw-mac fast-todo % docker-compose exec demo-app poetry add sqlalchemy aiomysql
Using version ^1.4.28 for SQLAlchemy
Using version ^0.0.22 for aiomysql

Updating dependencies
Resolving dependencies... (11.6s)

Writing lock file

Package operations: 4 installs, 0 updates, 0 removals

  • Installing greenlet (1.1.2)
  • Installing pymysql (0.9.3)
  • Installing aiomysql (0.0.22)
  • Installing sqlalchemy (1.4.28)
admin@gw-mac fast-todo % 
admin@gw-mac fast-todo % touch api/db.py
admin@gw-mac fast-todo % touch api/models/task.py
admin@gw-mac fast-todo % touch api/migrate_db.py
admin@gw-mac fast-todo % 
admin@gw-mac fast-todo % docker-compose exec demo-app poetry run python -m api.migrate_db
/src/.venv/lib/python3.9/site-packages/pymysql/cursors.py:170: Warning: (3719, "'utf8' is currently an alias for the character set UTF8MB3, but will be an alias for UTF8MB4 in a future release. Please consider using UTF8MB4 in order to be unambiguous.")
  result = self._query(query)
2021-12-10 12:55:48,800 INFO sqlalchemy.engine.Engine SHOW VARIABLES LIKE 'sql_mode'
2021-12-10 12:55:48,800 INFO sqlalchemy.engine.Engine [raw sql] {}
2021-12-10 12:55:48,829 INFO sqlalchemy.engine.Engine SHOW VARIABLES LIKE 'lower_case_table_names'
2021-12-10 12:55:48,829 INFO sqlalchemy.engine.Engine [generated in 0.00017s] {}
2021-12-10 12:55:48,838 INFO sqlalchemy.engine.Engine SELECT DATABASE()
2021-12-10 12:55:48,838 INFO sqlalchemy.engine.Engine [raw sql] {}
2021-12-10 12:55:48,840 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2021-12-10 12:55:48,840 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-10 12:55:48,840 INFO sqlalchemy.engine.Engine [generated in 0.00007s] {'table_schema': 'demo', 'table_name': 'tasks'}
2021-12-10 12:55:48,849 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-10 12:55:48,849 INFO sqlalchemy.engine.Engine [cached since 0.008605s ago] {'table_schema': 'demo', 'table_name': 'dones'}
2021-12-10 12:55:48,852 INFO sqlalchemy.engine.Engine COMMIT
2021-12-10 12:55:48,853 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2021-12-10 12:55:48,854 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-10 12:55:48,854 INFO sqlalchemy.engine.Engine [cached since 0.01357s ago] {'table_schema': 'demo', 'table_name': 'tasks'}
2021-12-10 12:55:48,857 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-10 12:55:48,857 INFO sqlalchemy.engine.Engine [cached since 0.01709s ago] {'table_schema': 'demo', 'table_name': 'dones'}
2021-12-10 12:55:48,860 INFO sqlalchemy.engine.Engine 
CREATE TABLE tasks (
        id INTEGER NOT NULL AUTO_INCREMENT, 
        title VARCHAR(1024), 
        PRIMARY KEY (id)
)


2021-12-10 12:55:48,860 INFO sqlalchemy.engine.Engine [no key 0.00013s] {}
2021-12-10 12:55:48,917 INFO sqlalchemy.engine.Engine 
CREATE TABLE dones (
        id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(id) REFERENCES tasks (id)
)


2021-12-10 12:55:48,917 INFO sqlalchemy.engine.Engine [no key 0.00010s] {}
2021-12-10 12:55:48,949 INFO sqlalchemy.engine.Engine COMMIT
admin@gw-mac fast-todo % 
```


# C: Create
```sh

```