import sqlite3
from app.models.Musique import Musique

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


    def get_by_auteur(self, auteur):

        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM musique WHERE auteur = ?", (auteur,))
        rows = cursor.fetchall()
        conn.close()

        return [Musique(*row) for row in rows]

    def get_by_genre(self, genre):

        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM musique WHERE genre = ?", (genre,))
        rows = cursor.fetchall()
        conn.close()

        return [Musique(*row) for row in rows]

    def get_by_date(self, date):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM musique WHERE date = ?", (date,))
        rows = cursor.fetchall()
        conn.close()

    def delete_musique(self, musique_id):

        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM musique WHERE id = ?", (musique_id,))
        conn.commit()
        conn.close()

