from app.DAO.PlaylistDAO import PlaylisteDAO
from app.models.Playliste import Playliste

class PlaylistService:
    def __init__(self):
        self.dao = PlaylisteDAO()

    def create_playlist(self, titre, auteur, genre, jour_prevu, entreprise):
        p = Playliste(
            titre=titre,
            auteur=auteur,
            genre=genre,
            jour_prevu=jour_prevu,
            entreprise=entreprise
        )
        self.dao.insert(p)
        return p

    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, playlist_id):
        return self.dao.get(playlist_id)

    def add_music_to_playlist(self, playlist_id, music):
        playlist = self.dao.get(playlist_id)
        if not playlist:
            raise ValueError("Playlist inexistante")

        playlist.MusiqueAJouer.append(music)
        self.dao.insert(playlist)
