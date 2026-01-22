import time
from datetime import datetime
import json


import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 2x pour pointer vers app plutôt que service

date_str = datetime.now().strftime("%Y-%m-%d")

LOGS_FILE = os.path.join(BASE_DIR, "programmeRaspberry", "logs", "logs[{date_str}].txt")


os.makedirs(os.path.dirname(LOGS_FILE), exist_ok=True)



def lecteur(folder, noms):
    pygame.mixer.init()

    # jouer musiques dans l'ordre fourni
    for nom in noms:
        # ajouter ".mp3" si absent
        fichier = nom if nom.lower().endswith(".mp3") else f"{nom}.mp3"
        chemin = os.path.join(folder, fichier)

        # Vérifier l’existence du fichier
        if not os.path.isfile(chemin):
            with open(LOGS_FILE, "a", encoding="utf-8") as f:
                f.write(
                    f"missing {chemin} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                )
            continue

        pygame.mixer.music.load(chemin)
        pygame.mixer.music.play()

        # Log de lecture
        with open(LOGS_FILE, "a", encoding="utf-8") as f:
            f.write(
                f"played {chemin} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            )

        # Attendre la fin de la lecture
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

# ugh=["TV2OP_OPKing_GnuSPECIALZ1156MBS_TBS28", "Magnificent_Machines_Steampunk"]

# lecteur("/home/darragh/Documents/work/sae/S301/MusiQuali/app/static/rasdata/allMusic", ugh)

def observateur(json_data, folder):
    jour_courant = datetime.now().strftime("%A").lower()
    print(jour_courant)
    if jour_courant not in json_data:
        return

    programme = json_data[jour_courant]


    heure_declenchement = programme[0]  # "HH:MM"
    print(heure_declenchement)
    playlist = programme[1:]

    heure_cible = datetime.strptime(heure_declenchement, "%H:%M").time()
    deja_joue = False

    while True:
        maintenant = datetime.now()

        if (maintenant.time() >= heure_cible and not deja_joue ):
            print(playlist)
            lecteur(folder, playlist)
            deja_joue = True

        # reset au changement de jour
        if maintenant.strftime("%A").lower() != jour_courant:
            break

        time.sleep(2)

while True:
    with open(
        "rasdata/rasjson.json",
        "r",
        encoding="utf-8"
    ) as f:
        json_data = json.load(f)
    print("a")
    observateur(
        json_data,
        "rasdata/allMusic"
    )

    time.sleep(30)
