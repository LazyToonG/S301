from flask import render_template, request
from app import app
from app.services.TraductionService import Traductionservice
#from app.controllers.LoginController import reqlogged
from app.services.service_schedule import service_schedule

ts = Traductionservice()


class IndexController:

    @app.route('/', methods=['GET'])
    def index():

        trad = ts.tradIndex()
        langue_choisie = request.args.get('lang')
        if langue_choisie not in ['fr', 'en']:
            langue_choisie = 'fr'
        textes = trad[langue_choisie]
        metadata = {"title": "Accueil", "pagename": "accueil"}
        return render_template('index.html', metadata=metadata, t=textes, current_lang=langue_choisie)