import os
from app.DAO.MusicDAO import MusicDAO
from mutagen.mp3 import MP3
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"mp3"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class MusiqueService:
    def __init__(self):
        self.dao = MusicDAO()
        self.upload_folder = UPLOAD_FOLDER
    
    def get_musiques(self, sort="title"):
        return self.dao.get_musiques(order_by=sort)

    def allowed_file(self, filename):
        return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

    def save_file(self, file):
        if file.filename == "":
            raise ValueError("Aucun fichier sélectionné")
        if not self.allowed_file(file.filename):
            raise ValueError("Format non autorisé")

        filename = secure_filename(file.filename)
        title = os.path.splitext(filename)[0]
        filepath = os.path.join(self.upload_folder, filename)
        file.save(filepath)

        audio = MP3(filepath) #mutagen pour gerer les mp3
        length = int(audio.info.length)

        # DAO retourne un objet Music
        return self.dao.create(title=title, path=filepath, length=length)

    def delete_musique(self, musique_id):
        self.dao.delete(musique_id)
