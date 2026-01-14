from flask import render_template
from app import app
#from app.controllers.LoginController import reqlogged

class IndexController:

    @app.route('/', methods=['GET'])
    def index():
        mode="sombre"
        metadata = {"title": "Accueil", "pagename": "accueil"}
        return render_template('login_v2.html', metadata=metadata, mode=mode)
