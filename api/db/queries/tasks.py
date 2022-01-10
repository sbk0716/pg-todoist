# CREATE
CREATE_TASK_QUERY = """
    INSERT INTO tasks (title, detail, created_at, updated_at)
    VALUES (:title, :detail, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
    RETURNING id, title, detail, created_at, updated_at;
"""

# READ
GET_ALL_TASK_WITH_DONE_QUERY = """
    SELECT tasks.id, tasks.title, tasks.detail, dones.id IS NOT NULL AS done, tasks.created_at, tasks.updated_at
    FROM tasks
    LEFT OUTER JOIN dones ON tasks.id = dones.id;
"""

GET_TASK_WITH_DONE_BY_ID_QUERY = """
    SELECT tasks.id, tasks.title, tasks.detail, dones.id IS NOT NULL AS done, tasks.created_at, tasks.updated_at
    FROM tasks
    LEFT OUTER JOIN dones ON tasks.id = dones.id
    WHERE tasks.id = :id;
"""

GET_TASK_BY_ID_QUERY = """
    SELECT tasks.id, tasks.title, tasks.detail, tasks.created_at, tasks.updated_at
    FROM tasks
    WHERE tasks.id = :id;
"""

# UPDATE
UPDATE_TASK_BY_ID_QUERY = """
    UPDATE tasks
    SET title = :title,
        detail = :detail,
        created_at = :created_at,
        updated_at = :updated_at
    WHERE id = :id
    RETURNING id, title, detail, created_at, updated_at;
"""

# DELETE
DELETE_TASK_BY_ID_QUERY = """
    DELETE FROM tasks
    WHERE id = :id
    RETURNING id, title, detail, created_at, updated_at;
"""
