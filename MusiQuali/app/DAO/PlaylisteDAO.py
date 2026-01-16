import sqlite3
from Playliste import Playliste
import Musique

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

    #dans une des colonnes de playliste il y a une concaténation des musiques a jouer et l'heure prévue
    #donc je fais des methodes pour concatener et déoncatener
    #c'est sans doute plus efficace de faire un table intermédiaire dans la bd mais je trouve que c plus drole de faire comme ca

    def _musiques_to_str(self, musiques):
        # MusiqueChoisie -> "id|id|id|id"
        return "|".join(
            f"{mc.musique.id}" 
            for mc in musiques
        )
    def _str_to_musiques(self, data):
        if not data:
            return []

        result = []
        for bloc in data.split("|"): #id|id|id|id...
            titre = bloc  
            result.append(Musique(titre))
        return result


#c'est qui l'ennemi des champignons?
#les champioui
    def insert(self, p: Playliste):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()

        musiques_str = self._musiques_to_str(p.MusiqueAJouer) #concat

        if p.id is None:
            cur.execute("""
                INSERT INTO playlist
                (titre, auteur, genre, date_cree, jour_prevu, entreprise, musiques)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                p.titre,
                
                p.genre,
                p.dateCrée,
                p.jourPrévu,
                p.Entreprise,
                musiques_str
            ))
            p.id = cur.lastrowid #donner id automatiquement
        else: # si la playliste existe déja , on fait une maj
            cur.execute("""
                UPDATE playlist
                SET titre=?, auteur=?, genre=?, date_cree=?, jour_prevu=?, entreprise=?, musiques=?
                WHERE id=?
            """, (
                p.titre,
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
            row[1], row[2], row[3], row[4], row[5], row[6], id=row[0]
        )

        p.MusiqueAJouer = self._str_to_musiques(row[7])
        return p

#je me rends compte que g codé avec des accents putain, c pas un des 7 pêchés ca?

    def getByX(self, field, value): #je fais une methode commmune à toutes que je réutilise vous avez vu le pro
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()

        cur.execute(f"SELECT * FROM playlist WHERE {field} = ?", (value,))
        rows = cur.fetchall()
        conn.close()

        result = []

        for row in rows:
            p = Playliste(
                row[1], row[2], row[3],row[4], row[5], row[6], id=row[0]
            )
            p.MusiqueAJouer = self._str_to_musiques(row[7])
            result.append(p)

        return result

    def getByEntreprise(self, entreprise):
        return self.getByX("entreprise", entreprise) #pas sur si on se sert de tous mais elles sont la si jamais.
    def getByJourPrevu(self, jour):
        return self.getByX("jour_prevu", jour)
    def getByDateCree(self, date):
        return self.getByX("date_cree", date)
    def getByTitre(self, titre):
        return self.getByX("titre", titre)
    def getByGenre(self, genre):
        return self.getByX("genre", genre)



