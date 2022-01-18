# 1. Project Overview
This is a project for an app called `ToDoIst`.

## (1)App Features
This app is able to use below function.

### User Story
- You can add any task.
- You can read the list of tasks.
- You can read the details of any task.
- You can edit any task.
- You can delete any task.
- You can mark the specified task as complete.
- You can mark the specified task as incomplete.


## (2)Project Structure
```sh
admin@gw-mac pg-todoist % tree -d
.
├── api
│   ├── core
│   ├── dependencies
│   ├── domain
│   │   └── models
│   ├── infra
│   │   ├── db
│   │   └── routers
│   ├── interfaces
│   │   ├── controllers
│   │   ├── db
│   │   │   ├── queries
│   │   │   └── repositories
│   │   └── schemas
│   └── usecases
├── db
├── migrations
│   └── versions
└── tests

19 directories
admin@gw-mac pg-todoist % 
```


# 2. Usage
## (1)poetry install
```sh
admin@gw-mac pg-todoist % docker-compose run --entrypoint "poetry install" app-api
Creating pg-todoist_app-api_run ... done
Installing dependencies from lock file

No dependencies to install or update
admin@gw-mac pg-todoist % 
```

## (2)docker-compose up
```sh
admin@gw-mac pg-todoist % docker image ls
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
admin@gw-mac pg-todoist % docker volume ls
DRIVER    VOLUME NAME
admin@gw-mac pg-todoist % 
admin@gw-mac pg-todoist % docker-compose up -d --build
Creating network "pg-todoist_default" with the default driver
Creating volume "pg-todoist_postgres_data" with default driver
...
...
Creating pg-todoist_app-db_1  ... done
Creating pg-todoist_app-api_1 ... done
admin@gw-mac pg-todoist % 
admin@gw-mac pg-todoist % docker image ls
REPOSITORY           TAG           IMAGE ID       CREATED         SIZE
pg-todoist_app-api   latest        5184743123b8   2 minutes ago   981MB
postgres             14.1-alpine   1149d285a5f5   12 days ago     209MB
admin@gw-mac pg-todoist % docker volume ls
DRIVER    VOLUME NAME
local     pg-todoist_postgres_data
admin@gw-mac pg-todoist % 
admin@gw-mac pg-todoist % docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS          PORTS                                         NAMES
11e38a66e34a   pg-todoist_app-api     "poetry run uvicorn …"   14 seconds ago   Up 13 seconds   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp     pg-todoist_app-api_1
51a9fb2883f5   postgres:14.1-alpine   "docker-entrypoint.s…"   14 seconds ago   Up 13 seconds   0.0.0.0:15432->5432/tcp, :::15432->5432/tcp   pg-todoist_app-db_1
admin@gw-mac pg-todoist % 
```

## (3)create schema and testdb
```sh
admin@gw-mac pg-todoist % docker-compose exec app-db /bin/ash
/ # 
/ # psql --username admin --dbname coredb
psql (14.1)
Type "help" for help.

coredb=# CREATE SCHEMA IF NOT EXISTS "todoist";
CREATE SCHEMA
coredb=# \dn
 List of schemas
  Name   | Owner 
---------+-------
 public  | admin
 todoist | admin
(2 rows)

coredb=# CREATE DATABASE "testdb";
CREATE DATABASE
coredb=# \l
                         List of databases
   Name    | Owner | Encoding | Collate | Ctype | Access privileges 
-----------+-------+----------+---------+-------+-------------------
 coredb    | admin | UTF8     | C       | C     | 
 postgres  | admin | UTF8     | C       | C     | 
 template0 | admin | UTF8     | C       | C     | =c/admin         +
           |       |          |         |       | admin=CTc/admin
 template1 | admin | UTF8     | C       | C     | =c/admin         +
           |       |          |         |       | admin=CTc/admin
 testdb    | admin | UTF8     | C       | C     | 
(5 rows) 
coredb=# 
coredb=# \c testdb
You are now connected to database "testdb" as user "admin".
testdb=# 
testdb=# CREATE SCHEMA IF NOT EXISTS "todoist";
CREATE SCHEMA
testdb=# 
testdb=# \q
/ # 
/ # exit
admin@gw-mac pg-todoist % 
```

## (4)migratation for app db
```sh
admin@gw-mac pg-todoist % docker-compose exec app-api /bin/bash
root@11e38a66e34a:/src# 
root@11e38a66e34a:/src# poetry run alembic current
POSTGRES_DB: coredb
execute run_migrations_online
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
root@11e38a66e34a:/src# 
root@11e38a66e34a:/src# poetry run alembic upgrade head
POSTGRES_DB: coredb
execute run_migrations_online
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> e5cc805f99e4, 1_create_tasks_and_dones_table
INFO  [alembic.runtime.migration] Running upgrade e5cc805f99e4 -> b430a6422cda, 2_add_status_type_column
root@11e38a66e34a:/src# 
root@11e38a66e34a:/src# poetry run alembic history --verbose
Rev: b430a6422cda (head)
Parent: e5cc805f99e4
Path: /src/migrations/versions/b430a6422cda_2_add_status_type_column.py

    2_add_status_type_column
    
    Revision ID: b430a6422cda
    Revises: e5cc805f99e4
    Create Date: 2022-01-16 08:09:12.304373

Rev: e5cc805f99e4
Parent: <base>
Path: /src/migrations/versions/e5cc805f99e4_1_create_tasks_and_dones_table.py

    1_create_tasks_and_dones_table
    
    Revision ID: e5cc805f99e4
    Revises: 
    Create Date: 2022-01-15 21:43:30.278141

root@11e38a66e34a:/src# 
```

## (5)docker-compose down
```sh
admin@gw-mac pg-todoist % docker-compose down
Removing pg-todoist_app-api_1 ... done
Removing pg-todoist_app-db_1  ... done
Removing network pg-todoist_default
admin@gw-mac pg-todoist % 
admin@gw-mac pg-todoist % docker volume ls
DRIVER    VOLUME NAME
local     pg-todoist_postgres_data
admin@gw-mac pg-todoist % 
admin@gw-mac pg-todoist % docker volume rm pg-todoist_postgres_data
pg-todoist_postgres_data
admin@gw-mac pg-todoist % 
admin@gw-mac pg-todoist % docker image ls
REPOSITORY           TAG           IMAGE ID       CREATED          SIZE
pg-todoist_app-api   latest        9d3acaa41821   11 minutes ago   981MB
postgres             14.1-alpine   1149d285a5f5   12 days ago      209MB
python               3.9-buster    5b9959224c95   3 weeks ago      830MB
admin@gw-mac pg-todoist % 
admin@gw-mac pg-todoist % docker image rm 9d3acaa41821
Untagged: pg-todoist_app-api:latest
Deleted: sha256:9d3acaa418210f3c49e0f9885ccca1fbdf70a336a5cb7a4013ed3ce6476b6f7b
admin@gw-mac pg-todoist % 
```


# 3. Generate migratation file
## (1)generate migratation file
```sh
admin@gw-mac pg-todoist % docker-compose exec app-api /bin/bash
root@589883599df0:/src# poetry run alembic revision --autogenerate -m "1_create_custom_schema_and_db"
POSTGRES_DB: coredb
execute run_migrations_online
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'todoist.tasks'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_todoist_tasks_status_type' on '['status_type']'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_todoist_tasks_title' on '['title']'
INFO  [alembic.autogenerate.compare] Detected added table 'todoist.dones'
INFO  [alembic.autogenerate.compare] Detected removed table 'alembic_version'
  Generating /src/migrations/versions/a0f37245c465_1_create_custom_schema_and_db.py ...  done
root@589883599df0:/src# 
```


# 4. operation verification
## (1)POST /api/tasks/
```sh
admin@gw-mac pg-todoist % curl -X 'POST' \
  'http://localhost:8000/api/tasks/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "歯医者",
  "detail": "来週のどこかで歯医者に行って虫歯を治す。"
}' | jq -r '.'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   272  100   170  100   102   2045   1227 --:--:-- --:--:-- --:--:--  3726
{
  "title": "歯医者",
  "detail": "来週のどこかで歯医者に行って虫歯を治す。",
  "id": 1,
  "created_at": "2021-12-26T20:51:10",
  "updated_at": "2021-12-26T20:51:10"
}
admin@gw-mac pg-todoist % 
```

## (2)GET /api/tasks/{task_id}/
```sh
admin@gw-mac pg-todoist % curl -X 'GET' \
  'http://localhost:8000/api/tasks/1/' \
  -H 'accept: application/json' | jq -r '.'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   183  100   183    0     0   8376      0 --:--:-- --:--:-- --:--:-- 15250
{
  "title": "歯医者",
  "detail": "来週のどこかで歯医者に行って虫歯を治す。",
  "id": 1,
  "done": false,
  "created_at": "2021-12-26T20:51:10",
  "updated_at": "2021-12-26T20:51:10"
}
admin@gw-mac pg-todoist % 
```

## (3)GET /api/tasks/
```sh
admin@gw-mac pg-todoist % curl -X 'GET' \
  'http://localhost:8000/api/tasks/' \
  -H 'accept: application/json' | jq -r '.'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   391  100   391    0     0  18406      0 --:--:-- --:--:-- --:--:-- 32583
[
  {
    "title": "歯医者",
    "detail": "来週のどこかで歯医者に行って虫歯を治す。",
    "id": 1,
    "done": false,
    "created_at": "2021-12-26T20:51:10",
    "updated_at": "2021-12-26T20:51:10"
  },
  {
    "title": "打ち合わせ",
    "detail": "今週の金曜日の13時からT社のUさんと打ち合わせを行う。",
    "id": 2,
    "done": false,
    "created_at": "2021-12-26T20:54:36",
    "updated_at": "2021-12-26T20:54:36"
  }
]
admin@gw-mac pg-todoist % 
```

## (4)PUT /api/tasks/{task_id}/
```sh
admin@gw-mac pg-todoist % curl -X 'PUT' \
  'http://localhost:8000/api/tasks/2/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "打ち合わせ",
  "detail": "今週の金曜日の8時からKさんと打ち合わせを行う。"
}' | jq -r '.'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   300  100   184  100   116   6602   4162 --:--:-- --:--:-- --:--:-- 15789
{
  "title": "打ち合わせ",
  "detail": "今週の金曜日の8時からKさんと打ち合わせを行う。",
  "id": 2,
  "created_at": "2021-12-26T20:54:36",
  "updated_at": "2021-12-26T20:57:11"
}
admin@gw-mac pg-todoist % 
```

## (5)PUT /api/tasks/{task_id}/done/
```sh
admin@gw-mac pg-todoist % curl -X 'PUT' \
  'http://localhost:8000/api/tasks/2/done/' \
  -H 'accept: application/json' | jq -r '.'

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    33  100    33    0     0    820      0 --:--:-- --:--:-- --:--:--  1100
{
  "message": "create_done | ID: 2"
}
admin@gw-mac pg-todoist % 
```

## (6)DELETE /api/tasks/{task_id}/done/
```sh
admin@gw-mac pg-todoist % curl -X 'DELETE' \
  'http://localhost:8000/api/tasks/2/done/' \
  -H 'accept: application/json' | jq -r '.'

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    33  100    33    0     0   1551      0 --:--:-- --:--:-- --:--:--  2357
{
  "message": "delete_done | ID: 2"
}
admin@gw-mac pg-todoist % 
```

## (7)DELETE /api/tasks/{task_id}/
```sh
admin@gw-mac pg-todoist % curl -X 'DELETE' \
  'http://localhost:8000/api/tasks/2/' \
  -H 'accept: application/json' | jq -r '.'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   184  100   184    0     0   5338      0 --:--:-- --:--:-- --:--:--  7360
{
  "title": "打ち合わせ",
  "detail": "今週の金曜日の8時からKさんと打ち合わせを行う。",
  "id": 2,
  "created_at": "2021-12-26T20:54:36",
  "updated_at": "2021-12-26T20:57:11"
}
admin@gw-mac pg-todoist % 
```


# 5. Lint and Format
## (1)poetry run flake8
```sh
admin@gw-mac pg-todoist % docker-compose exec app-api /bin/bash
root@aef0a7ee5af8:/src# 
root@aef0a7ee5af8:/src# poetry run flake8 api db tests
db/client.py:38:11: F541 f-string is missing placeholders
root@aef0a7ee5af8:/src# 
```

## (2)poetry run black
```sh
admin@gw-mac pg-todoist % docker-compose exec app-api /bin/bash
root@aef0a7ee5af8:/src# 
root@aef0a7ee5af8:/src# poetry run black api db tests
All done! ✨ 🍰 ✨
32 files left unchanged.
root@aef0a7ee5af8:/src# 
```


# 5. Test
## (1)set up postgresql
```sh
admin@gw-mac pg-todoist % docker-compose exec app-api /bin/bash
root@c6ea00e01944:/src# python db/pg_client.py
==================================================
1. SELECT datname, datdba, encoding, datcollate, datctype from pg_database
==================================================
(datname, datdba, encoding, datcollate, datctype)
--------------------------------------------------
('postgres', 10, 6, 'C', 'C')
('coredb', 10, 6, 'C', 'C')
('template1', 10, 6, 'C', 'C')
('template0', 10, 6, 'C', 'C')
('testdb', 10, 6, 'C', 'C')
==================================================
==================================================
2. SELECT usename, usesysid, usecreatedb, usesuper, passwd FROM pg_user
==================================================
(usename, usesysid, usecreatedb, usesuper, passwd)
--------------------------------------------------
('admin', 10, True, True, '********')
('root', 16394, False, True, '********')
==================================================
root@c6ea00e01944:/src# 
```

## (2)migratation for test db
```sh
admin@gw-mac pg-todoist % docker-compose exec app-api /bin/bash
root@c6ea00e01944:/src# export ENV=test
root@c6ea00e01944:/src# printenv | grep ENV
ENV=test
root@c6ea00e01944:/src# poetry run alembic current
POSTGRES_DB: testdb
execute run_migrations_online
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
root@c6ea00e01944:/src# 
root@c6ea00e01944:/src# poetry run alembic upgrade head
POSTGRES_DB: testdb
execute run_migrations_online
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> e5cc805f99e4, 1_create_tasks_and_dones_table
INFO  [alembic.runtime.migration] Running upgrade e5cc805f99e4 -> b430a6422cda, 2_add_status_type_column
root@c6ea00e01944:/src# 
root@c6ea00e01944:/src# poetry run alembic current
POSTGRES_DB: testdb
execute run_migrations_online
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
b430a6422cda (head)
root@c6ea00e01944:/src# 
```

## (3)poetry run pytest
```sh
root@c6ea00e01944:/src# poetry run pytest -v --cov=.
========================================== test session starts ==========================================
platform linux -- Python 3.9.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /src/.venv/bin/python
cachedir: .pytest_cache
rootdir: /src, configfile: pyproject.toml, testpaths: tests
plugins: anyio-3.4.0, asyncio-0.16.0, cov-3.0.0
collected 6 items                                                                                       

tests/test_dones.py::TestCrudDones::test_done_flag PASSED                                         [ 16%]
tests/test_health.py::TestHealth::test_health_check PASSED                                        [ 33%]
tests/test_tasks.py::TestCrudTasks::test_create_task_and_read_task PASSED                         [ 50%]
tests/test_tasks.py::TestCrudTasks::test_create_task_and_update_task PASSED                       [ 66%]
tests/test_tasks.py::TestCrudTasks::test_create_task_and_delete_task PASSED                       [ 83%]
tests/test_tasks.py::TestCrudTasks::test_create_all_task_and_read_all_task PASSED                 [100%]

----------- coverage: platform linux, python 3.9.9-final-0 -----------
Name                                         Stmts   Miss  Cover
----------------------------------------------------------------
api/__init__.py                                  0      0   100%
api/core/__init__.py                             0      0   100%
api/core/environ.py                             18      1    94%
api/core/logging.py                              3      0   100%
api/dependencies/__init__.py                     0      0   100%
api/dependencies/db.py                          12      0   100%
api/domain/__init__.py                           0      0   100%
api/domain/models/__init__.py                    0      0   100%
api/domain/models/task.py                       23      0   100%
api/infra/__init__.py                            0      0   100%
api/infra/db/__init__.py                         0      0   100%
api/infra/db/connection.py                      25     12    52%
api/infra/routers/__init__.py                    8      0   100%
api/infra/routers/dones.py                      27      4    85%
api/infra/routers/health.py                      6      0   100%
api/infra/routers/tasks.py                      34      4    88%
api/interfaces/__init__.py                       0      0   100%
api/interfaces/db/__init__.py                    0      0   100%
api/interfaces/db/queries/__init__.py            0      0   100%
api/interfaces/db/queries/dones.py               3      0   100%
api/interfaces/db/queries/tasks.py               6      0   100%
api/interfaces/db/repositories/__init__.py       0      0   100%
api/interfaces/db/repositories/base.py           4      0   100%
api/interfaces/db/repositories/dones.py         49     15    69%
api/interfaces/db/repositories/tasks.py        107     35    67%
api/interfaces/schemas/__init__.py               0      0   100%
api/interfaces/schemas/done.py                  17      0   100%
api/interfaces/schemas/task.py                  33      0   100%
api/main.py                                     15      2    87%
tests/__init__.py                                0      0   100%
tests/conftest.py                               39     10    74%
tests/test_dones.py                             21      0   100%
tests/test_health.py                            11      0   100%
tests/test_tasks.py                             99      0   100%
----------------------------------------------------------------
TOTAL                                          560     83    85%


========================================== 6 passed in 27.76s ===========================================
root@c6ea00e01944:/src# 
```