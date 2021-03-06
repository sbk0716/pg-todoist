# ====================
# CREATE
# ====================
CREATE_TASK_QUERY = """
INSERT INTO todoist.tasks
    (title, detail, status_type, created_at, updated_at)
VALUES
    (:title, :detail, :status_type, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
RETURNING
    id, title, detail, status_type, created_at, updated_at;
"""

# ====================
# READ
# ====================
GET_ALL_TASK_WITH_DONE_QUERY = """
SELECT
    tasks.id,
    tasks.title,
    tasks.detail,
    tasks.status_type,
    dones.id IS NOT NULL AS done,
    tasks.created_at,
    tasks.updated_at
FROM
    todoist.tasks
LEFT OUTER JOIN
    todoist.dones
ON
    todoist.tasks.id = todoist.dones.id;
"""

GET_TASK_WITH_DONE_BY_ID_QUERY = """
SELECT
    tasks.id,
    tasks.title,
    tasks.detail,
    tasks.status_type,
    dones.id IS NOT NULL AS done,
    tasks.created_at,
    tasks.updated_at
FROM
    todoist.tasks
LEFT OUTER JOIN
    todoist.dones
ON
    todoist.tasks.id = todoist.dones.id
WHERE
    tasks.id = :id;
"""

GET_TASK_BY_ID_QUERY = """
SELECT
    tasks.id,
    tasks.title,
    tasks.detail,
    tasks.created_at,
    tasks.updated_at
FROM
    todoist.tasks
WHERE
    tasks.id = :id;
"""

# ====================
# UPDATE
# ====================
UPDATE_TASK_BY_ID_QUERY = """
UPDATE todoist.tasks
SET
    title = :title,
    detail = :detail,
    status_type = :status_type,
    created_at = :created_at,
    updated_at = :updated_at
WHERE
    id = :id
RETURNING
    id, title, detail, status_type, created_at, updated_at;
"""

# ====================
# DELETE
# ====================
DELETE_TASK_BY_ID_QUERY = """
DELETE FROM todoist.tasks
WHERE
    id = :id
RETURNING
    id, title, detail, status_type, created_at, updated_at;
"""
