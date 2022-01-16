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
admin@gw-mac simple-fastapi % tree -d
.
├── api
│   ├── core
│   ├── dependencies
│   ├── domain
│   │   └── models
│   ├── infra
│   │   ├── db
│   │   └── routers
│   └── interfaces
│       ├── db
│       │   ├── queries
│       │   └── repositories
│       └── schemas
├── db
├── migrations
│   └── versions
└── tests

17 directories
admin@gw-mac simple-fastapi % 
```


# 2. Usage

## (1)docker-compose up
```sh
admin@gw-mac fast-todo % docker image ls
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
admin@gw-mac fast-todo % docker volume ls
DRIVER    VOLUME NAME
admin@gw-mac fast-todo % 
admin@gw-mac fast-todo % docker-compose up -d --build
Creating network "fast-todo_default" with the default driver
Creating volume "fast-todo_mysql_data" with default driver
Building app-api
[+] Building 2.1s (11/11) FINISHED   
...
...
Creating fast-todo_app-db_1  ... done
Creating fast-todo_app-api_1 ... done
admin@gw-mac fast-todo % 
admin@gw-mac fast-todo % docker image ls
REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
fast-todo_app-api   latest    5380a020174b   24 minutes ago   959MB
mysql               8.0       bbf6571db497   9 days ago       516MB
admin@gw-mac fast-todo % 
admin@gw-mac fast-todo % docker volume ls
DRIVER    VOLUME NAME
local     fast-todo_mysql_data
admin@gw-mac fast-todo % 
admin@gw-mac fast-todo % docker ps
CONTAINER ID   IMAGE               COMMAND                  CREATED         STATUS         PORTS                                                    NAMES
c47c5b30908f   fast-todo_app-api   "poetry run uvicorn …"   2 minutes ago   Up 2 minutes   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp                fast-todo_app-api_1
390c305998df   mysql:8.0           "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   33060/tcp, 0.0.0.0:13306->3306/tcp, :::13306->3306/tcp   fast-todo_app-db_1
admin@gw-mac fast-todo % 
```

## (2)generate migratation file for app db
```sh
admin@gw-mac simple-fastapi % docker-compose exec app-api /bin/bash
root@bd6bc0f7ab71:/src# poetry run alembic revision --autogenerate -m "1_create_tasks_and_dones_table"
POSTGRES_DB: coredb
execute run_migrations_online
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.ddl.postgresql] Detected sequence named 'tasks_id_seq' as owned by integer column 'tasks(id)', assuming SERIAL and omitting
  Generating /src/migrations/versions/a349ab64cdd1_1_create_tasks_and_dones_table.py ...  done
root@bd6bc0f7ab71:/src# 
root@8025b42a4ce1:/src# poetry run black .
reformatted migrations/versions/2b699da13ffa_update_tasks_column.py
All done! ✨ 🍰 ✨
1 file reformatted, 34 files left unchanged.
root@8025b42a4ce1:/src# 
```

## (3)migratation for app db
```sh
admin@gw-mac fast-todo % docker-compose exec app-api /bin/bash
root@82aa92de72bf:/src# poetry run alembic upgrade +1
POSTGRES_DB: coredb
execute run_migrations_online
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> e5cc805f99e4, 1_create_tasks_and_dones_table
root@82aa92de72bf:/src# 
root@82aa92de72bf:/src# poetry run alembic history --verbose
Rev: e5cc805f99e4 (head)
Parent: <base>
Path: /src/migrations/versions/e5cc805f99e4_1_create_tasks_and_dones_table.py

    1_create_tasks_and_dones_table
    
    Revision ID: e5cc805f99e4
    Revises: 
    Create Date: 2022-01-15 21:43:30.278141

root@82aa92de72bf:/src# 
```

## (4)docker-compose down
```sh
admin@gw-mac fast-todo % docker-compose down
Stopping fast-todo_app-api_1 ... done
Stopping fast-todo_app-db_1  ... done
Removing fast-todo_app-api_1 ... done
Removing fast-todo_app-db_1  ... done
Removing network fast-todo_default
admin@gw-mac fast-todo % 
admin@gw-mac fast-todo % docker volume ls
DRIVER    VOLUME NAME
local     fast-todo_mysql_data
admin@gw-mac fast-todo % 
admin@gw-mac fast-todo % docker volume rm fast-todo_mysql_data
fast-todo_mysql_data
admin@gw-mac fast-todo % docker image ls
REPOSITORY          TAG       IMAGE ID       CREATED             SIZE
fast-todo_app-api   latest    5380a020174b   About an hour ago   959MB
mysql               8.0       bbf6571db497   9 days ago          516MB
admin@gw-mac fast-todo % docker image rm 5380a020174b         
Untagged: fast-todo_app-api:latest
Deleted: sha256:5380a020174bcdd5156f1f8931b8a1116379fa052b5650ef8e496ed115e610d6
admin@gw-mac fast-todo % 
```


# 3. operation verification

## (1)POST /api/tasks/
```sh
admin@gw-mac fast-todo % curl -X 'POST' \
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
admin@gw-mac fast-todo % 
```

## (2)GET /api/tasks/{task_id}/
```sh
admin@gw-mac fast-todo % curl -X 'GET' \
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
admin@gw-mac fast-todo % 
```

## (3)GET /api/tasks/
```sh
admin@gw-mac fast-todo % curl -X 'GET' \
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
admin@gw-mac fast-todo % 
```

## (4)PUT /api/tasks/{task_id}/
```sh
admin@gw-mac fast-todo % curl -X 'PUT' \
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
admin@gw-mac fast-todo % 
```

## (5)PUT /api/tasks/{task_id}/done/
```sh
admin@gw-mac fast-todo % curl -X 'PUT' \
  'http://localhost:8000/api/tasks/2/done/' \
  -H 'accept: application/json' | jq -r '.'

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    33  100    33    0     0    820      0 --:--:-- --:--:-- --:--:--  1100
{
  "message": "create_done | ID: 2"
}
admin@gw-mac fast-todo % 
```

## (6)DELETE /api/tasks/{task_id}/done/
```sh
admin@gw-mac fast-todo % curl -X 'DELETE' \
  'http://localhost:8000/api/tasks/2/done/' \
  -H 'accept: application/json' | jq -r '.'

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    33  100    33    0     0   1551      0 --:--:-- --:--:-- --:--:--  2357
{
  "message": "delete_done | ID: 2"
}
admin@gw-mac fast-todo % 
```

## (7)DELETE /api/tasks/{task_id}/
```sh
admin@gw-mac fast-todo % curl -X 'DELETE' \
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
admin@gw-mac fast-todo % 
```


# 4. Lint and Format and Test

## (1)set up postgresql
```sh
admin@gw-mac simple-fastapi % docker-compose exec app-api /bin/bash
root@82aa92de72bf:/src# python db/pg_client.py
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
('root', 67260, False, True, '********')
==================================================
root@82aa92de72bf:/src# 
```

## (2)migratation for test db
```sh
admin@gw-mac fast-todo % docker-compose exec app-api /bin/bash
root@82aa92de72bf:/src# export ENV=test
root@82aa92de72bf:/src# printenv | grep ENV
ENV=test
root@82aa92de72bf:/src# poetry run alembic current
POSTGRES_DB: testdb
execute run_migrations_online
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
root@82aa92de72bf:/src# 
root@82aa92de72bf:/src# poetry run alembic upgrade head
POSTGRES_DB: testdb
execute run_migrations_online
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> e5cc805f99e4, 1_create_tasks_and_dones_table
root@82aa92de72bf:/src# 
root@82aa92de72bf:/src# poetry run alembic current
POSTGRES_DB: testdb
execute run_migrations_online
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
e5cc805f99e4 (head)
root@82aa92de72bf:/src# 
```


## (3)poetry run flake8
```sh
root@aef0a7ee5af8:/src# export ENV=test
root@aef0a7ee5af8:/src# printenv | grep ENV
ENV=test
root@aef0a7ee5af8:/src# 
root@aef0a7ee5af8:/src# poetry run flake8 api db tests
db/client.py:38:11: F541 f-string is missing placeholders
root@aef0a7ee5af8:/src# 
```


## (4)poetry run black
```sh
root@aef0a7ee5af8:/src# export ENV=test
root@aef0a7ee5af8:/src# printenv | grep ENV
ENV=test
root@aef0a7ee5af8:/src# 
root@aef0a7ee5af8:/src# poetry run black api db tests
All done! ✨ 🍰 ✨
32 files left unchanged.
root@aef0a7ee5af8:/src# 
```


## (5)poetry run pytest
```sh
root@82aa92de72bf:/src# poetry run pytest -v --cov=.
========================================= test session starts ==========================================
platform linux -- Python 3.9.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /src/.venv/bin/python
cachedir: .pytest_cache
rootdir: /src, configfile: pyproject.toml, testpaths: tests
plugins: anyio-3.4.0, asyncio-0.16.0, cov-3.0.0
collected 6 items                                                                                      

tests/test_dones.py::TestCrudDones::test_done_flag PASSED                                        [ 16%]
tests/test_health.py::TestHealth::test_health_check PASSED                                       [ 33%]
tests/test_tasks.py::TestCrudTasks::test_create_task_and_read_task PASSED                        [ 50%]
tests/test_tasks.py::TestCrudTasks::test_create_task_and_update_task PASSED                      [ 66%]
tests/test_tasks.py::TestCrudTasks::test_create_task_and_delete_task PASSED                      [ 83%]
tests/test_tasks.py::TestCrudTasks::test_create_all_task_and_read_all_task PASSED                [100%]

----------- coverage: platform linux, python 3.9.9-final-0 -----------
Name                                         Stmts   Miss  Cover
----------------------------------------------------------------
api/__init__.py                                  0      0   100%
api/core/__init__.py                             0      0   100%
api/core/environ.py                             18      1    94%
api/core/logging.py                              3      0   100%
api/dependencies/__init__.py                     0      0   100%
api/dependencies/db.py                          16      0   100%
api/domain/__init__.py                           0      0   100%
api/domain/models/__init__.py                    0      0   100%
api/domain/models/task.py                       29      0   100%
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
api/interfaces/db/repositories/tasks.py        101     35    65%
api/interfaces/schemas/__init__.py               0      0   100%
api/interfaces/schemas/done.py                  17      0   100%
api/interfaces/schemas/task.py                  32      0   100%
api/main.py                                     15      2    87%
tests/__init__.py                                0      0   100%
tests/conftest.py                               39     10    74%
tests/test_dones.py                             20      0   100%
tests/test_health.py                            11      0   100%
tests/test_tasks.py                             90      0   100%
----------------------------------------------------------------
TOTAL                                          553     83    85%


========================================== 6 passed in 37.79s ==========================================
root@82aa92de72bf:/src# 
```