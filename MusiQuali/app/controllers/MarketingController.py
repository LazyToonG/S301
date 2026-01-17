# app/controllers/MarketingController.py
from flask import render_template, request, redirect, url_for, abort, session
from app import app
from app.controllers.LoginController import reqrole
from app.services.MusiqueService import MusiqueService

service = MusiqueService()

class MarketingController:

    @app.route('/marketing', methods=['GET'])
    @reqrole("marketing")
    def marketing():

        langue_url = request.args.get('lang')
        
        if langue_url:
            session['langue'] = langue_url
            langue_choisie = langue_url
        else:
            langue_choisie = session.get('langue')

        textes = service.get_traductions(langue_choisie)

        sort = request.args.get("sort", "date")
        musiques = service.get_musiques(sort)

        metadata = {"title": "Espace Marketing", "pagename": "marketing"}
        return render_template("marketing_v2.html", metadata=metadata, sort=sort, t=textes, current_lang=langue_choisie, musiques=musiques)

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

    @app.route("/upload", methods=["POST"])
    def upload():
        file = request.files.get("audio")
        if not file:
            abort(400, "No file part")

        try:
            result = service.save_file(file)
            return f"MP3 uploaded successfully: {result['filename']} ({result['duration']}s)", 200
        except ValueError as e:
            abort(400, str(e))
        except Exception as e:
            abort(500, f"Internal server error: {str(e)}")
