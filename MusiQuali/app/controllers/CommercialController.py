from flask import render_template, request, redirect, url_for
from app import app
from app.controllers.LoginController import reqrole

class CommercialController:

    @app.route('/commercial', methods=['GET'])
    @reqrole("commercial")
    def commercial_dashboard():
        metadata = {"title": "Espace Commercial", "pagename": "commercial"}
        return render_template('commercial/index.html', metadata=metadata)

    @app.route('/commercial/message/urgent', methods=['POST'])
    @reqrole("commercial")
    def send_urgent_message():
        contenu = request.form.get("message")
        return redirect(url_for("commercial_dashboard"))
