class Traductionservice():

    def tradIndex(self):
        return {
            'fr': {
                "login" : "Se connecter",
                'titre': "Bienvenue sur Musi-quali, votre plateforme de diffusion sonore",
                'desc_1': "Musi-quali est une plateforme qui vous permettra de diffuser de la musique et des messages sonores dans votre établissement. Vous pouvez préparer à l'avance un planning de musiques et de messages de publicité directement en ligne, faire des annonces quand vous voulez, et notre plateforme marche même en cas de coupure de connexion.",
                'desc_2': "Besoin d'une ambiance sonore dans votre magasin ? Utilisez Musi-quali !",
                'equipe_intro': "Nous somme une équipe d'éudiants en deuxième année en BUT Informatique à l'Universitée Sorbonne Paris Nord.",
                'equipe_liste': "Notre équipe est composée de :"
            },
            'en': {
                "login" : "Login",
                'titre': "Welcome to Musi-quali, your sound broadcasting platform",
                'desc_1': "Musi-quali is a platform that allows you to broadcast music and audio messages in your establishment. You can prepare a schedule of music and advertising messages in advance directly online, make announcements whenever you want, and our platform even works in the event of a connection failure.",
                'desc_2': "Need a sound atmosphere in your store? Use Musi-quali!",
                'equipe_intro': "We are a team of second-year students studying for a Bachelor's degree in Computer Science at Sorbonne Paris Nord University.",
                'equipe_liste': "Our team consists of:"
            }
        }
    
    def tradLogin(self):
        return {
            "fr" : {
                "user" : "Utilisateur",
                "logout" : "Déconnexion",
                "index" : "Accueil",
                "h1" : "Nom d'utilisateur",
                "password" : "Mot de passe",
                "role" : "Rôle",
                "connexion" : "Connexion",
                "create" : "Créer",
                "commercial" : "Commercial (Défaut)",
                "marketing" : "Marketing",
                "admin" : "Administrateur"
            },

            "en" : {
                "user" : "User",
                "logout" : "Logout",
                "index" : "Home",
                "h1" : "Username",
                "role" : "Role",
                "password" : "Password",
                "connexion" : "Login",
                "create" : "Create",
                "commercial" : "Commercial (Default)",
                "marketing" : "Marketing",
                "admin" : "Administrator"
            }
        }
    
    def tradAdmin(self):
        return {
            "fr" : {
                "user" : "Utilisateur",
                "logout" : "Déconnexion",
                "btn_rouge_1" : "Messages (accès page message)",
                "btn_rouge_2" : "Mettre à jour les M3U",
                "btn_rouge_3" : "Playlist (accès page playlist)",
                "btn_rouge_4" : "Base de données (accès BD)",
                "btn_rouge_5" : "Créer un nouvel utilisateur",
                "q_form_1" : "Quel est l'identifiant de la nouvelle Raspberry que vous voulez insérer ?",
                "q_form_2" : "Quel est l'adresse IP de cette nouvelle Raspberry que vous voulez insérer ?",
                "t_form_1" : "Entrez l'identifiant de la Raspberry",
                "t_form_2" : "Entrez l'adresse IP de la Raspberry",
                "valider" : "Validez",
                "refresh" : "Dernier rafraîchissement",
                "notes" : "Notes",
                "contacts" : "Contacts",
                "h1" : "Nom d'utilisateur",
                "password" : "Mot de passe",
                "role" : "Rôle",
                "connexion" : "Connexion",
                "create" : "Créer",
                "commercial" : "Commercial (Défaut)",
                "marketing" : "Marketing",
                "admin" : "Administrateur"
            },

            "en" : {
                "user" : "User",
                "logout" : "Logout",
                "btn_rouge_1" : "Messages (access message page)",
                "btn_rouge_2" : "Update the M3U files",
                "btn_rouge_3" : "Playlist (access playlist page)",
                "btn_rouge_4" : "Database (DB access)",
                "btn_rouge_5" : "Create a new user",
                "q_form_1" : "What is the ID of the new Raspberry you want to insert?",
                "q_form_2" : "What is the IP address of this new Raspberry Pi that you want to insert?",
                "t_form_1" : "Enter the Raspberry ID",
                "t_form_2" : "Enter the IP address of the Raspberry",
                "valider" : "Validate",
                "refresh" : "Last refresh",
                "notes" : "Notes",
                "contacts" : "Contacts",
                "h1" : "Username",
                "role" : "Role",
                "password" : "Password",
                "connexion" : "Login",
                "create" : "Create",
                "commercial" : "Commercial (Default)",
                "marketing" : "Marketing",
                "admin" : "Administrator"
            }
        }
    
    def tradCommercial(self):
        return {
            "fr" : {
                "user" : "Utilisateur",
                "logout" : "Déconnexion",
                "h3_1" : "Jouer un message",
                "h3_2" : "Télécharger un nouveau message",
                "p" : "Importer un message vocal"
            },

            "en" : {
                "user" : "User",
                "logout" : "Logout",
                "h3_1" : "Play a message",
                "h3_2" : "Upload a new message",
                "p" : "Import a voice message"
            }
        }
    
    def tradMarketing(self):
        return {
            'fr': {
                "user" : "Utilisateur",
                "logout" : "Déconnexion",
                "play" : "Jouer playlist",
                "shuffle" : "Lecture aléatoire",
                "titre" : "Titre",
                "genre" : "Genre",
                "date" : "Date",
                "auteur" : "Artiste",
                "h3" : "Glisser-déposer ou cliquez pour sélectionner un fichier",
                "h3_1" : "Créer une nouvelle playlist",
                "nom" : "Nom de la playlist",
                "creer" : "Créer",
                "select" : "Choisir une playlist",
                "select_value" : "— Sélectionner —",
                "upload" : "Veuillez sélectionner une playlist",
                "submit" : "Envoyer",
                "convertir" : "Besoin de convertir en mp3?"
            },
            'en': {
                "user" : "User",
                "logout" : "Logout",
                "play" : "Play playlist",
                "shuffle" : "Shuffle playlist",
                "titre" : "Title",
                "genre" : "Genre",
                "date" : "Date",
                "auteur" : "Artist",
                "h3" : "Drag and drop or click to select a file",
                "h3_1" : "Create a new playlist",
                "nom" : "Playlist name",
                "creer" : "Create",
                "select" : "Select a playlist",
                "select_value" : "— Select —",
                "upload" : "Select a playlist",
                "submit" : "Send",
                "convertir" : "Need to convert to mp3?"
            }
        }