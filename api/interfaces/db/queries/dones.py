# ====================
# CREATE
# ====================
CREATE_DONE_QUERY = """
    INSERT INTO dones (id, note, created_at, updated_at)
    VALUES (:id, :note, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
    RETURNING id, note, created_at, updated_at;
"""

# ====================
# READ
# ====================
GET_DONE_BY_ID_QUERY = """
    SELECT dones.id, dones.note, dones.created_at, dones.updated_at
    FROM dones
    WHERE id = :id;
"""

# ====================
# DELETE
# ====================
DELETE_DONE_BY_ID_QUERY = """
    DELETE FROM dones
    WHERE id = :id
    RETURNING id, note, created_at, updated_at;
"""
