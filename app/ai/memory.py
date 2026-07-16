import sqlite3


class Memory:

    def __init__(self):

        self.conn = sqlite3.connect("jarvis_memory.db")

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory(

            key TEXT PRIMARY KEY,

            value TEXT
        )
        """)

        self.conn.commit()

    def save(self, key, value):

        self.cursor.execute(
            "REPLACE INTO memory VALUES (?, ?)",
            (key, value)
        )

        self.conn.commit()

    def recall(self, key):

        self.cursor.execute(
            "SELECT value FROM memory WHERE key=?",
            (key,)
        )

        row = self.cursor.fetchone()

        if row:
            return row[0]

        return None