from flask import render_template, request
from app import app
from app.controllers.LoginController import reqrole
from app.services.TraductionService import Traductionservice

ts = Traductionservice()

class AdminController:

    @app.route('/admin', methods=['GET'])
    @reqrole("admin")
    def admin_dashboard():
        traductions=ts.tradAdmin()
        
        langue_choisie = request.args.get('lang')
        if langue_choisie not in ['fr', 'en']:
            langue_choisie = 'fr'
        textes = traductions[langue_choisie]

        metadata = {"title": "Panel Admin", "pagename": "admin"}

        data = {
            "messages_diffuses": [],
            "etat_lecteurs": [],
            "playlist_ok": True,
        }

        return render_template('admin.html', metadata=metadata, data=data, t=textes, current_lang=langue_choisie)

    @app.route('/admin/playlist/resync', methods=['POST'])
    @reqrole("admin")
    def resync_playlist():
        pass

    @app.route('/admin/playlist/update', methods=['POST'])
    @reqrole("admin")
    def update_playlist():
        pass

    @app.route('/admin/alert', methods=['POST'])
    @reqrole("admin")
    def trigger_alert():
        pass