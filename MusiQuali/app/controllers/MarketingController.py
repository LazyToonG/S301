# app/controllers/MarketingController.py
from flask import render_template, request, redirect, url_for, abort, session
from app import app
from app.controllers.LoginController import reqrole
from app.services.MusiqueService import MusiqueService
from app.services.playlistServiceMarketing import PlaylistService

service = MusiqueService()
playlist_service = PlaylistService()

class MarketingController:

    @app.route('/marketing', methods=['GET'])
    def marketing():

        langue_url = request.args.get('lang')
        
        if langue_url:
            session['langue'] = langue_url
            langue_choisie = langue_url
        else:
            langue_choisie = session.get('langue')

        """textes = service.get_traductions(langue_choisie)"""

        sort = request.args.get("sort", "date")
        musiques = service.get_musiques(sort)

        metadata = {"title": "Espace Marketing", "pagename": "marketing"}
        return render_template("marketing_v2.html", metadata=metadata, sort=sort, current_lang=langue_choisie, musiques=musiques , t=service)

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

    @app.route("/playlist/create", methods=["POST"])
    @reqrole("marketing")
    def create_playlist():
        titre = request.form.get("titre")

        if not titre:
            abort(400, "Titre de playlist obligatoire")

        playlist_service.create_playlist(
            titre=titre,
            auteur="marketing",
            genre=None,
            jour_prevu=None,
            entreprise=None
        )

        return redirect(url_for("marketing"))


    @app.route("/upload", methods=["POST"])#upload
    @reqrole("marketing")
    def upload():
        file = request.files.get("audio")
        playlist_id = request.form.get("playlist_id")

        # sécurité
        if not file:
            abort(400, "Aucun fichier envoyé")
        # sécurité aussi
        if not playlist_id:
            abort(400, "Aucune playlist sélectionnée")

        playlist = playlist_service.get_by_id(int(playlist_id))

        if not playlist:
            abort(400, "Playlist invalide")

        try:
            # sauvegarde via MusiqueService
            result = service.save_file(file)

            # ajout à la playliste
            playlist_service.add_music_to_playlist(
                playlist.id,
                result["music"]  # Music(result["id"]) 
            )

            return redirect(url_for("marketing"))

        except ValueError as e: #sécurité
            abort(400, str(e))
        except Exception as e:
            abort(500, f"Internal server error: {str(e)}")