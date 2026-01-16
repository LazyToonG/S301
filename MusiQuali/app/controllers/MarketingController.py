from flask import render_template, request, redirect, url_for, Flask, abort
from app import app
import os
from app.controllers.LoginController import reqrole

from MusiQuali.app.DAO.MusiqueDAO import MusiqueDAO

app = Flask(__name__)
dao = MusiqueDAO()

@app.route("/")
def index():
    traductions={}
    langue_choisie = request.args.get('lang')
    if langue_choisie not in ['fr', 'en']:
        langue_choisie = 'fr'
    textes = traductions[langue_choisie]

    sort = request.args.get("sort", "date")
    musiques = dao.get_5_musiques(sort)
    return render_template("index.html", musiques=musiques, sort=sort)

@app.route("/delete/<int:id>")
def delete(id):
    dao.delete_musique(id)
    return redirect(url_for("index"))

@app.route("/search_by_titre")
def search_by_titre():
    titre = request.args.get("titre")
    if titre:
        musiques = dao.get_by_titre(titre)
        return render_template("index.html", musiques=musiques)
    return redirect(url_for("index"))


@app.route("/search_by_auteur")
def search_by_auteur():
    auteur = request.args.get("auteur")
    if auteur:
        musiques = dao.get_by_auteur(auteur)
        return render_template("index.html", musiques=musiques)
    return redirect(url_for("index"))


#Upload de mp3

UPLOAD_FOLDER = "uploads"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB conseillé (suffisant+sécu)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE

ALLOWED_EXTENSIONS = {"mp3"} #fichiers autorisés

os.makedirs(UPLOAD_FOLDER, exist_ok=True) #créer dossier
#mettre dans /tsatic/data
def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS, 
    )

#fdp va
@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["audio"]

    if file.filename == "":
        abort(400, "No selected file")

    if not allowed_file(file.filename):
        abort(400, "Only MP3 files allowed")

    # Sécurité,     anti injection
    from werkzeug.utils import secure_filename
    filename = secure_filename(file.filename)

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)#construit db



    return "MP3 uploaded successfully", 200


#import sqlite3

#conn = sqlite3.connect("music.db")
#cursor = conn.cursor()

#cursor.execute(
  #  "INSERT INTO songs (filename, filepath, mimetype, size) VALUES (?, ?, ?, ?)",
 #   (filename, filepath, file.mimetype, os.path.getsize(filepath))
#)

#conn.commit()
#conn.close()