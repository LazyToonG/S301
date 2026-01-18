import sqlite3
from app.models.Playliste import Playliste
import os

class PlaylisteDAO:

    def __init__(self, db_path=None):#le chemin relatif plantait mais pas le chemin absolu et g fini par demander a chatgpt qui a proposé ca
        # Determine absolute path to database inside project
        if db_path is None:
            # Adjust this relative to your project root
            project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            db_path = os.path.join(project_root, "static/data/database.db")
        
        # Ensure parent directories exist
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        self.db = db_path
        print("Connecting to database at:", self.db)
        self._init_db()


    def _init_db(self):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(playlist)")
        print(cursor.fetchall())
        conn.execute("""
            CREATE TABLE IF NOT EXISTS playlist (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                music_ids TEXT
            )
        """)
        conn.close()

    def _ids_to_str(self, ids):
        return "|".join(str(i) for i in ids)

    def _str_to_ids(self, data):
        return [int(i) for i in data.split("|")] if data else []

    def insert(self, playlist: Playliste):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()

        music_ids_str = self._ids_to_str(playlist.music_ids)

        if playlist.id is None:
            cur.execute(
                "INSERT INTO playlist (title, music_ids) VALUES (?, ?)",
                (playlist.title, music_ids_str)
            )
            playlist.id = cur.lastrowid
        else:
            cur.execute(
                "UPDATE playlist SET title=?, music_ids=? WHERE id=?",
                (playlist.title, music_ids_str, playlist.id)
            )

        conn.commit()
        conn.close()

    def get(self, playlist_id):
        conn = sqlite3.connect(self.db)
        row = conn.execute(
            "SELECT id, title, music_ids FROM playlist WHERE id=?",
            (playlist_id,)
        ).fetchone()
        conn.close()

        if not row:
            return None

        return Playliste(
            id=row[0],
            title=row[1],
            music_ids=self._str_to_ids(row[2])
        )

    def get_all(self):
        conn = sqlite3.connect(self.db)
        rows = conn.execute("SELECT id, title, music_ids FROM playlist").fetchall()
        conn.close()

        return [
            Playliste(
                id=row[0],
                title=row[1],
                music_ids=self._str_to_ids(row[2])
            )
            for row in rows
        ]
