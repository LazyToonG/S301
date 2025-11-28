from flask import render_template
from app import app
from app.controllers.LoginController import reqrole

class MarketingController:

    @app.route('/marketing', methods=['GET'])
    @reqrole("marketing")
    def marketing_dashboard():
        metadata = {"title": "Espace marketing", "pagename": "marketing"}
        return render_template('marketing/index.html', metadata=metadata)

    @app.route('/marketing/music/add', methods=['POST'])
    @reqrole("marketing")
    def add_music():

    @app.route('/marketing/music/delete', methods=['POST'])
    @reqrole("marketing")
    def delete_music():
