# app/controllers/MarketingController.py
from flask import render_template, request, redirect, url_for, abort, session
from app import app
from app.controllers.LoginController import reqrole
from app.services.MusiqueService import MusiqueService
from app.services.playlistServiceMarketing import PlaylistService
from app.services.TraductionService import Traductionservice

ts = Traductionservice()
service = MusiqueService()
playlist_service = PlaylistService()

@app.route('/marketing', methods=['GET', 'POST'])
@reqrole("admin","marketing")
def marketing():
    # Translations
    traductions = ts.tradMarketing()
    langue_choisie = ts.getLangue()
    textes = traductions[langue_choisie]

    # Page content
    playlists = playlist_service.get_all()
    sort = request.args.get("sort", "date")
    musiques = service.get_musiques(sort)
    user = session['username']
    role = session['role']
    metadata = {"title": "Espace Marketing", "pagename": "marketing"}

    # Playlist selection
    selected_playlist_id = None
    musics = []

    if request.method == "POST":
        playlist_id_raw = request.form.get("playlist_id")
        if playlist_id_raw:
            # Convert type to match your playlist IDs
            selected_playlist_id = str(playlist_id_raw)  
            musics = playlist_service.musics_in_playlist(selected_playlist_id)

    return render_template(
        "marketing_v2.html",
        metadata=metadata,
        sort=sort,
        current_lang=langue_choisie,
        musiques=musiques,
        t=textes,
        playlists=playlists,
        user=user,
        role=role,
        musics=musics,
        selected_playlist_id=selected_playlist_id
    )



@app.route("/delete/<int:id>")
def delete(id):
    service.delete_musique(id)
    return redirect(url_for("marketing"))

@app.route("/search_by_title")
def search_by_title():
    traductions=ts.tradMarketing()
    langue_url = request.args.get('lang')
        
    langue_choisie=ts.getLangue()
    textes = traductions[langue_choisie]
    user = session['username']
    role = session['role']

    title = request.args.get("title")
    musiques = service.search_by_title(title)
    if musiques:
        return render_template("marketing_v2.html", musiques=[musiques], t=textes, current_lang=langue_choisie, user=user, role=role)
    return redirect(url_for("marketing"))

@app.route("/playlist/create", methods=["POST"])
def create_playlist():
    title = request.form.get("title")
    if not title:
        abort(400, "Title de playlist obligatoire")

    playlist_service.create_playlist(title=title)
    return redirect(url_for("marketing"))


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("audio")
    playlist_id = request.form.get("playlist_id")

    if not file or not playlist_id:
        abort(400, "Fichier ou playlist manquant")

    playlist = playlist_service.get_by_id(int(playlist_id))
    if not playlist:
        abort(400, "Playlist invalide")

    music = service.save_file(file)
    playlist_service.add_music_to_playlist(playlist.id, music.id)

    return redirect(url_for("marketing"))

# @app.route("/musicsinplaylist", methods=["GET", "POST"])
# def musicsinplaylist():

#     t = ts.getLangue()

#     playlist_id = request.values.get("playlist_id")

#     playlists = playlist_service.get_all()

#     musics = []
#     if playlist_id:
#         musics = playlist_service.musics_in_playlist(playlist_id)

#     return render_template(
#         "marketing_v2.html",
#         playlists=playlists,
#         musics=musics,
#         selected_playlist_id=playlist_id,
#         t=t
#     )


