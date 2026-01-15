from flask import render_template, request
from app import app
#from app.controllers.LoginController import reqlogged

class IndexController:

    @app.route('/', methods=['GET'])
    def index():
        traductions = {
            'fr': {
                'titre': "Bienvenue sur Musi-quali, votre plateforme de diffusion sonore",
                'desc_1': "Musi-quali est une plateforme qui vous permettra de diffuser de la musique et des messages sonores dans votre établissement. Vous pouvez préparer à l'avance un planning de musiques et de messages de publicité directement en ligne, faire des annonces quand vous voulez, et notre plateforme marche même en cas de coupure de connexion.",
                'desc_2': "Besoin d'une ambiance sonore dans votre magasin ? Utilisez Musi-quali !",
                'equipe_intro': "Nous somme une équipe d'éudiants en deuxième année en BUT Informatique à l'Universitée Sorbonne Paris Nord.",
                'equipe_liste': "Notre équipe est composée de :"
            },
            'en': {
                'titre': "Welcome to Musi-quali, your sound broadcasting platform",
                'desc_1': "Musi-quali is a platform that allows you to broadcast music and audio messages in your establishment. You can prepare a schedule of music and advertising messages in advance directly online, make announcements whenever you want, and our platform even works in the event of a connection failure.",
                'desc_2': "Need a sound atmosphere in your store? Use Musi-quali!",
                'equipe_intro': "We are a team of second-year students studying for a Bachelor's degree in Computer Science at Sorbonne Paris Nord University.",
                'equipe_liste': "Our team consists of:"
            }
        }
        langue_choisie = request.args.get('lang')
        if langue_choisie not in ['fr', 'en']:
            langue_choisie = 'fr'
        textes = traductions[langue_choisie]
        metadata = {"title": "Accueil", "pagename": "accueil"}
<<<<<<< HEAD
        return render_template('index.html', metadata=metadata, t=textes, current_lang=langue_choisie)
=======
        return render_template('admin.html', metadata=metadata, t=textes, current_lang=langue_choisie)
>>>>>>> 56187d30dc076fac997330071ca9a8fe4e87d0b5
