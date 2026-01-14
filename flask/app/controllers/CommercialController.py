from flask import render_template, request, redirect, url_for
from app import app
from app.controllers.LoginController import reqrole

class CommercialController:


    @app.route('/commercial', methods=['GET'])
    @reqrole("commercial")
    def commercial_dashboard():
        traductions={
            "fr" : {
                "h3_1" : "Jouer un message",
                "h3_2" : "Upload un nouveau message",
                "p" : "Importer message vocal"
            },

            "en" : {
                "h3_1" : "Play a message",
                "h3_2" : "Upload a new message",
                "p" : "Message vocal de l'importateur"
            }
        }
        langue_choisie = request.args.get('lang')
        if langue_choisie not in ['fr', 'en']:
            langue_choisie = 'fr'
        textes = traductions[langue_choisie]

        metadata = {"title": "Espace Commercial", "pagename": "commercial"}
        return render_template('commercial.html', metadata=metadata)

    @app.route('/commercial/message/urgent', methods=['POST'])
    @reqrole("commercial")
    def send_urgent_message():
        contenu = request.form.get("message")
        return redirect(url_for("commercial_dashboard"))
