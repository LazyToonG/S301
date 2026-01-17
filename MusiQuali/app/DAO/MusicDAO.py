import sqlite3
from app.models.Musique import Musique
from app import app
from mutagen.mp3 import MP3

class MusicDAO:


    def get_connection(self):
        conn = sqlite3.connect(app.static_folder + '/data/database.db')
        conn.row_factory = sqlite3.Row
        return conn

    def get_musiques(self, order_by="titre"):
        """ordre par defaut c'est titres'"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, artist, path FROM music")
        rows = cursor.fetchall()
        conn.close()

        return [Musique(*row) for row in rows]

    def get_by_titre(self, titre):

        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, artist, path FROM music WHERE title = ?", (titre,))
        row = cursor.fetchone()
        conn.close()

        return Musique(*row) if row else None


    def create(self, title, length, path, playlist_id):
        conn = self.get_connection()
        conn.execute('INSERT INTO music (title, duration, path, playlist_id) VALUES (?, ?, ?, ?)',
                     (title, int(length), path, playlist_id))
        conn.commit()
        conn.close() 

    def delete_musique(self, musique_id):

        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM music WHERE id = ?", (musique_id,))
        conn.commit()
        conn.close()

    def get_by_playlist_id(self, playlist_id):
        conn = self.get_connection()
        musics = conn.execute('SELECT * FROM music WHERE playlist_id = ?', (playlist_id,)).fetchall()
        conn.close()
        return musics
