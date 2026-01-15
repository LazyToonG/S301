from MusiQuali.app.models import Musique


class Playliste:
    def __init__(self, titre, auteur, genre, dateCrée, jourPrévu, Entreprise, id=None):
        self.id=id # pour lui assigner un id automatiquement + tard quand on le met dans la bd
        self.titre = titre
        self.genre = genre
        self.dateCrée = dateCrée #les 3 pour le tri dans la vue , jsp si on se servira de tous les filtres mais je mets au cas ou
        self.jourPrévu = jourPrévu
        self.Entreprise = Entreprise # ca dépend de comment on fait la bd 
        self.MusiqueAJouer = []
        #un objet peut avoir en attribut un autre (= composition si il en dépend sinon agregation)
        #g crée un objet ChoixMusique qui sera pris en argument, c'est le titre d'une musique et une heure. 
        #il y a sans doute un meilleur moyen de faire, notemment avec les dictionnaires mais bon
  
    def addMusique(self, MusiqueChoisie):
        self.MusiqueAJouer.append(MusiqueChoisie)

class MusiqueChoisie:
    def __init__(self, musique: Musique, heure: str):
        self.musique = musique
        self.heure = heure


    