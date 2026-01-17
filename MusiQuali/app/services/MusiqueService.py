import os
from app.DAO.MusiqueDAO import MusiqueDAO
from app.services.TraductionService import Traductionservice
from mutagen.mp3 import MP3
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "uploads"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_EXTENSIONS = {"mp3"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

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

    def __init__(self):
        self.dao = MusiqueDAO()
        self.upload_folder = UPLOAD_FOLDER

    def allowed_file(self, filename):
        return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

    def save_file(self, file, playlist_id=None):
        if file.filename == "":
            raise ValueError("Aucun fichier selectionné")
        if not self.allowed_file(file.filename):
            raise ValueError("fichiers autorisés : {ALLOWED_EXTENSIONS}")

        filename = secure_filename(file.filename)
        filepath = os.path.join(self.upload_folder, filename)
        file.save(filepath)

        # mutagen pour extraire metadonnées
        audio = MP3(filepath)
        duration = int(audio.info.length)  # ( en secondes)

        # appelle create de musiqueDAO
        self.dao.create(title=filename, length=duration, path=filepath, playlist_id=playlist_id)

        return {"filename": filename, "duration": duration, "path": filepath}
