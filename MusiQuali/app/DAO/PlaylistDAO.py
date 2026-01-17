import sqlite3
from app.models.Playliste import Playliste
from app.models.Music import Music
from app.models.db import get_db

class PlaylisteDAO:
    def __init__(self, db="database.db"):
        self.db = db
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS playlist (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titre TEXT,
                auteur TEXT,
                genre TEXT,
                date_cree TEXT,
                jour_prevu TEXT,
                entreprise TEXT,
                musiques TEXT
            )
        """)
        conn.close()

    def _musiques_to_str(self, musiques):
        return "|".join(str(m.id) for m in musiques)

    def _str_to_musiques(self, data):
        if not data:
            return []
        return [Music(id=int(mid)) for mid in data.split("|")]

    def insert(self, p: Playliste):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()

        musiques_str = self._musiques_to_str(p.MusiqueAJouer)

        if p.id is None:
            cur.execute("""
                INSERT INTO playlist
                (titre, auteur, genre, date_cree, jour_prevu, entreprise, musiques)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                p.titre,
                p.auteur,
                p.genre,
                p.dateCrée,
                p.jourPrévu,
                p.Entreprise,
                musiques_str
            ))
            p.id = cur.lastrowid
        else:
            cur.execute("""
                UPDATE playlist
                SET titre=?, auteur=?, genre=?, date_cree=?, jour_prevu=?, entreprise=?, musiques=?
                WHERE id=?
            """, (
                p.titre,
                p.auteur,
                p.genre,
                p.dateCrée,
                p.jourPrévu,
                p.Entreprise,
                musiques_str,
                p.id
            ))

        conn.commit()
        conn.close()

    def get(self, id):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute("SELECT * FROM playlist WHERE id=?", (id,))
        row = cur.fetchone()
        conn.close()

        if not row:
            return None

        p = Playliste(
            titre=row[1],
            auteur=row[2],
            genre=row[3],
            date_cree=row[4],
            jour_prevu=row[5],
            entreprise=row[6],
            id=row[0]
        )
        p.MusiqueAJouer = self._str_to_musiques(row[7])
        return p

    def get_all(self):
        conn = sqlite3.connect(self.db)
        rows = conn.execute("SELECT * FROM playlist").fetchall()
        conn.close()

        playlists = []
        for row in rows:
            p = Playliste(
                row[1], row[2], row[3], row[4], row[5], row[6], id=row[0]
            )
            p.MusiqueAJouer = self._str_to_musiques(row[7])
            playlists.append(p)

        return playlists
