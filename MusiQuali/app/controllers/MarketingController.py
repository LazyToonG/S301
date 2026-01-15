from flask import render_template, request, redirect, url_for, Flask
from app import app
from app.controllers.LoginController import reqrole

from app.models.MusiqueDAO import MusiqueDAO

app = Flask(__name__)
dao = MusiqueDAO()

class MarketingController:

    @app.route('/marketing', methods=['GET'])
    def index():
        traductions = {
            'fr': {
                "user" : "Utilisateur",
                "logout" : "Déconnexion"
            },
            'en': {
                "user" : "User",
                "logout" : "Logout"
            }
        }
        langue_choisie = request.args.get('lang')
        if langue_choisie not in ['fr', 'en']:
            langue_choisie = 'fr'
        textes = traductions[langue_choisie]

        sort = request.args.get("sort", "date")
        musiques = dao.get_5_musiques(sort)
        return render_template("marketing_v2.html", musiques=musiques, sort=sort, t=textes, current_lang=langue_choisie)

@app.route("/delete/<int:id>")
def delete(id):
    dao.delete_musique(id)
    return redirect(url_for("index"))

@app.route("/search_by_titre")
def search_by_titre():
    titre = request.args.get("titre")
    if titre:
        musiques = dao.get_by_titre(titre)
        return render_template("marketing_v2.html", musiques=musiques)
    return redirect(url_for("index"))


@app.route("/search_by_auteur")
def search_by_auteur():
    auteur = request.args.get("auteur")
    if auteur:
        musiques = dao.get_by_auteur(auteur)
        return render_template("marketing_v2.html", musiques=musiques)
    return redirect(url_for("index"))
