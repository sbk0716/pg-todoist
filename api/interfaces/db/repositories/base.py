from databases import Database


class BaseRepository:
    def __init__(self, db: Database) -> None:
        """
        Set the connection pool to `BaseRepository instance`.
        """
        self.db = db
