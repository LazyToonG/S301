from flask import render_template, request
from app import app
from app.controllers.LoginController import reqrole

class AdminController:

    @app.route('/admin', methods=['GET'])
    @reqrole("admin")
    def admin_dashboard():
        traductions={
            "fr" : {
                "user" : "Utilisateur",
                "logout" : "Déconnexion",
                "btn_rouge_1" : "Messages (accès page message)",
                "btn_rouge_2" : "Mettre à jour les M3U",
                "btn_rouge_3" : "Playlist (accès page playlist)",
                "btn_rouge_4" : "Base de données (accès BD)",
                "q_form_1" : "Quel est l'identifiant de la nouvelle Raspberry que vous voulez insérer ?",
                "q_form_2" : "Quel est l'adresse IP de cette nouvelle Raspberry que vous voulez insérer ?",
                "t_form_1" : "Entrez l'identifiant de la Raspberry",
                "t_form_2" : "Entrez l'adresse IP de la Raspberry",
                "refresh" : "Dernier rafraîchissement",
                "notes" : "Notes",
                "contacts" : "Contacts"
            },

            "en" : {
                "user" : "User",
                "logout" : "Logout",
                "btn_rouge_1" : "Messages (access message page)",
                "btn_rouge_2" : "Update the M3U files",
                "btn_rouge_3" : "Playlist (access playlist page)",
                "btn_rouge_4" : "Database (DB access)",
                "q_form_1" : "What is the ID of the new Raspberry you want to insert?",
                "q_form_2" : "What is the IP address of this new Raspberry Pi that you want to insert?",
                "t_form_1" : "Enter the Raspberry ID",
                "t_form_2" : "Enter the IP address of the Raspberry",
                "refresh" : "Last refresh",
                "notes" : "Notes",
                "contacts" : "Contacts"
            }
        }
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