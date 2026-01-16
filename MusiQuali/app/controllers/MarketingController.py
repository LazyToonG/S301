# app/controllers/MarketingController.py
from flask import render_template, request, redirect, url_for, abort
from app import app
from app.controllers.LoginController import reqrole
from app.services.MarketingService import MarketingService

service = MarketingService()

class MarketingController:

    @app.route('/marketing', methods=['GET'])
    @reqrole("marketing")
    def marketing():
        langue_choisie = request.args.get('lang', 'fr')
        textes = service.get_traductions(langue_choisie)

        sort = request.args.get("sort", "date")
        musiques = service.get_musiques(sort)

        metadata = {"title": "Espace Marketing", "pagename": "marketing"}
        return render_template(
            "marketing_v2.html",
            metadata=metadata,
            sort=sort,
            t=textes,
            current_lang=langue_choisie,
            musiques=musiques
        )

    @app.route("/delete/<int:id>")
    def delete(id):
        service.delete_musique(id)
        return redirect(url_for("marketing"))

    @app.route("/search_by_titre")
    def search_by_titre():
        titre = request.args.get("titre")
        musiques = service.search_by_titre(titre)
        if musiques:
            return render_template("marketing_v2.html", musiques=[musiques])
        return redirect(url_for("marketing"))

    @app.route("/search_by_auteur")
    def search_by_auteur():
        auteur = request.args.get("auteur")
        musiques = service.search_by_auteur(auteur)
        if musiques:
            return render_template("marketing_v2.html", musiques=musiques)
        return redirect(url_for("marketing"))
