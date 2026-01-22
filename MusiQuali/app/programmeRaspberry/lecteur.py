import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

from datetime import datetime # 2. Pour la date et l'heure


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #2x pour pointer vers app plutot que service

# Set upload folder relative to the app structure
LOGS_FILE = os.path.join(BASE_DIR, "static", "data", "logs.txt")


# Make sure the folder exists
os.makedirs(LOGS_FILE, exist_ok=True)



def lecteur(folder): #folder=chemin vers dossier

    pygame.mixer.init()

    LOG_FILE = LOGS_FILE
    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]
    for fichier in mp3_files: #parcourir les mp3
        chemin = os.path.join(folder, fichier) #chemin du mp3 actuel
        pygame.mixer.music.load(chemin)
        pygame.mixer.music.play()
        with open(LOG_FILE, "a") as f: #ouvrir logs
            f.write(
                f"played {chemin} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            )
# attendre la fin de la lecture
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

#jq      cat monfichier.json | jq ....> toto.m3u ; vlc mp3