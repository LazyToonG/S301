import sqlite3
from app.models.Musique import Musique
#from mutagen.mp3 import MP3

class MusiqueDAO:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def get_musiques(self, order_by="titre"):
        """ordre pardefaut c'est titres'"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(f"""SELECT * FROM musique ORDER BY {order_by} ASC LIMIT 5""")
        rows = cursor.fetchall()
        conn.close()

        return [Musique(*row) for row in rows]

    def get_by_titre(self, titre):

        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM musique WHERE titre = ?", (titre,))
        row = cursor.fetchone()
        conn.close()

        return Musique(*row) if row else None


    def create(self, title, length, path, playlist_id):
        conn = self.get_db()
        conn.execute('INSERT INTO music (title, duration, path, playlist_id) VALUES (?, ?, ?, ?)',
                     (title, int(length), path, playlist_id))
        conn.commit()
        conn.close() 

    def delete_musique(self, musique_id):

        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM musique WHERE id = ?", (musique_id,))
        conn.commit()
        conn.close()

    