from datetime import datetime, date, timedelta
from Playliste import Playliste


class Lundi:
    def __init__(self, entreprise, Playlist:Playliste):
        self.entreprise=entreprise
        self.Playlist=Playlist

class Mardi:
    def __init__(self, entreprise, Playlist:Playliste):
        self.entreprise=entreprise
        self.Playlist=Playlist 
class Mercredi:
    def __init__(self, entreprise, Playlist:Playliste):
        self.entreprise=entreprise
        self.Playlist=Playlist  
class Jeudi:
    def __init__(self, entreprise, Playlist:Playliste):
        self.entreprise=entreprise
        self.Playlist=Playlist

class Vendredi:
    def __init__(self, entreprise, Playlist:Playliste):
        self.entreprise=entreprise
        self.Playlist=Playlist  
class Samedi:
    def __init__(self, entreprise, Playlist:Playliste):
        self.entreprise=entreprise
        self.Playlist=Playlist

class Dimanche:
    def __init__(self, entreprise, Playlist:Playliste):
        self.entreprise=entreprise
        self.Playlist=Playlist
        #je vais les afficher indépendamment.
        #manque DAO