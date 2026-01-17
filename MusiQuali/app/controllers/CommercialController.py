from flask import render_template, request, redirect, url_for, session
from app import app
from app.controllers.LoginController import reqrole
from app.services.TraductionService import Traductionservice

ts = Traductionservice()

class CommercialController:

    @app.route('/commercial', methods=['GET'])
    @reqrole("commercial")
    def commercial_dashboard():
        traductions=ts.tradCommercial()

        langue_url = request.args.get('lang')
        
        if langue_url:
            session['langue'] = langue_url
            langue_choisie = langue_url
        else:
            langue_choisie = session.get('langue')

        if langue_choisie not in ['fr', 'en']:
            langue_choisie = 'fr'
        textes = traductions[langue_choisie]

        metadata = {"title": "Espace Commercial", "pagename": "commercial"}
        return render_template('commercial.html', metadata=metadata, t=textes, current_lang=langue_choisie)

    @app.route('/commercial/message/urgent', methods=['POST'])
    @reqrole("commercial")
    def send_urgent_message():
        contenu = request.form.get("message")
        return redirect(url_for("commercial_dashboard"))
