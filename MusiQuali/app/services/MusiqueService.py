
from app.DAO.MusiqueDAO import MusiqueDAO
from app.services.TraductionService import Traductionservice

class MusiqueService:
    def __init__(self):
        self.dao = MusiqueDAO()
        self.ts = Traductionservice()

    def get_traductions(self, lang):
        if lang not in ['fr', 'en']:
            lang = 'fr'#au cas ou on se sert de langues jsp
        traductions = self.ts.tradMarketing()
        return traductions[lang]

    def get_musiques(self, sort="date"):
        return self.dao.get_musiques(order_by=sort)

    def search_by_titre(self, titre):
        if titre:
            return self.dao.get_by_titre(titre)
        return None


    def delete_musique(self, musique_id):
        self.dao.delete_musique(musique_id)
