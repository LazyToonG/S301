import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

from datetime import datetime # 2. Pour la date et l'heure


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 2x pour pointer vers app plutôt que service

date_str = datetime.now().strftime("%Y-%m-%d")

LOGS_FILE = os.path.join(BASE_DIR, "programmeRaspberry", "logs", "logs[{date_str}].txt")

# Créer uniquement le dossier parent
os.makedirs(os.path.dirname(LOGS_FILE), exist_ok=True)



def lecteur(folder, noms):
    pygame.mixer.init()

    # Construire la playlist dans l’ordre fourni
    for nom in noms:
        # Ajouter .mp3 si absent
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

ugh=["TV2OP_OPKing_GnuSPECIALZ1156MBS_TBS28", "Magnificent_Machines_Steampunk"]

lecteur("/home/darragh/Documents/work/sae/S301/MusiQuali/app/static/rasdata/allMusic", ugh)