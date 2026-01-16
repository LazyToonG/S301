from flask import render_template, request, redirect, url_for, Flask
from app import app
from app.controllers.LoginController import reqrole

from app.models.MusiqueDAO import MusiqueDAO

#app = Flask(__name__)
dao = MusiqueDAO()

class MarketingController:

    @app.route('/marketing', methods=['GET'])
    @reqrole("marketing")
    def marketing():
        traductions = {
            'fr': {
                "user" : "Utilisateur",
                "logout" : "Déconnexion",
                "play" : "Jouer playlist",
                "shuffle" : "Lecture aléatoire",
                "titre" : "Titre",
                "genre" : "Genre",
                "date" : "Date",
                "auteur" : "Artiste",
                "h3" : "Télécharger une nouvelle musique",
                "p" : "Glisser le fichier ici"
            },
            'en': {
                "user" : "User",
                "logout" : "Logout",
                "play" : "Play playlist",
                "shuffle" : "Shuffle playlist",
                "titre" : "Title",
                "genre" : "Genre",
                "date" : "Date",
                "auteur" : "Artist",
                "h3" : "Download new music",
                "p" : "Drag the file here"
            }
        }
        langue_choisie = request.args.get('lang')
        if langue_choisie not in ['fr', 'en']:
            langue_choisie = 'fr'
        textes = traductions[langue_choisie]

        sort = request.args.get("sort", "date")
        #musiques = dao.get_5_musiques(sort)

        metadata = {"title": "Espace Marketing", "pagename": "marketing"}
        return render_template("marketing_v2.html", metadata=metadata, sort=sort, t=textes, current_lang=langue_choisie)

    @app.route("/delete/<int:id>")
    def delete(id):
        dao.delete_musique(id)
        return redirect(url_for("marketing"))

    @app.route("/search_by_titre")
    def search_by_titre():
        titre = request.args.get("titre")
        if titre:
            musiques = dao.get_by_titre(titre)
            return render_template("marketing_v2.html", musiques=musiques)
        return redirect(url_for("marketing"))


    @app.route("/search_by_auteur")
    def search_by_auteur():
        auteur = request.args.get("auteur")
        if auteur:
            musiques = dao.get_by_auteur(auteur)
            return render_template("marketing_v2.html", musiques=musiques)
        return redirect(url_for("marketing"))
