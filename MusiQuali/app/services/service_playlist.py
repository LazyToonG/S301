from app.DAO.PlaylistDAO import PlaylisteDAO
from app.DAO.MusicDAO import MusicDAO

class PlaylistService:
    def __init__(self):
        self.playlist_dao = PlaylisteDAO()
        self.music_dao = MusicDAO()

    def get_all_playlists(self):
        return self.playlist_dao.get_all()

    def create_playlist(self, name):
        self.playlist_dao.create(name)

    def get_playlists_api_data(self):
        playlists = self.playlist_dao.get_all()
        data = {}
        for pl in playlists:
            musics = self.music_dao.get_by_playlist_id(pl['id'])
            data[pl['name']] = [{
                'name': m['title'], 
                'artist': m['artist'], 
                'path': m['path'], 
                'length': m['duration']
            } for m in musics]
        return data

service_playlist = PlaylistService()