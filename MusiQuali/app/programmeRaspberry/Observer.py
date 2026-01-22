import time
from datetime import datetime
from lecteur import lecteur
import json

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
        "/home/darragh/Documents/work/sae/S301/MusiQuali/app/programmeRaspberry/jsontest.json",
        "r",
        encoding="utf-8"
    ) as f:
        json_data = json.load(f)
    print("a")
    observateur(
        json_data,
        "/home/darragh/Documents/work/sae/S301/MusiQuali/app/static/rasdata/allMusic"
    )

    time.sleep(30)
