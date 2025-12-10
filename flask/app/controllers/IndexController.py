from flask import render_template
from app import app
#from app.controllers.LoginController import reqlogged

class IndexController:

    @app.route('/', methods=['GET'])
    def index():
        metadata = {"title": "Accueil", "pagename": "index"}
        return render_template('index.html', metadata=metadata)
