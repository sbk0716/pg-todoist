CREATE_TASK_QUERY = """
    INSERT INTO tasks (title, detail, created_at, updated_at)
    VALUES (:title, :detail, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
    RETURNING id, title, detail, created_at, updated_at;
"""

GET_ALL_TASK_WITH_DONE_QUERY = """
    SELECT tasks.id, tasks.title, tasks.detail, dones.id IS NOT NULL AS done, tasks.created_at, tasks.updated_at
    FROM tasks
    LEFT OUTER JOIN dones ON tasks.id = dones.id;
"""

GET_TASK_WITH_DONE_QUERY = """
    SELECT tasks.id, tasks.title, tasks.detail, dones.id IS NOT NULL AS done, tasks.created_at, tasks.updated_at
    FROM tasks
    LEFT OUTER JOIN dones ON tasks.id = dones.id
    WHERE tasks.id = :id;
"""
