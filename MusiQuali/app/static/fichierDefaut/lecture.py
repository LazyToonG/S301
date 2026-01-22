import pygame #gère le son/multimédia
import os #permet de lister les fichiers dans un dossier
import time #gère le temps

def lancer_playlist(): #définit une fonction
    
    pygame.mixer.init() #allume pygame sans sa pas de musique
    fichiers = os.listdir(".") #liste tous ce qu'il ya sur le fichier
    print("--- Début de la lecture ---") #pas besoin de vous dire sa affiche le texte
    for musique in fichiers:
        if musique.endswith(".mp3"):
            try:
                print(f"Lecture de : {musique}")
                pygame.mixer.music.load(musique) #affiche le nom de la musique en cours
                pygame.mixer.music.play() #Charge le fichier dans le lecteur.
                while pygame.mixer.music.get_busy(): #get_busy() renvoie True tant que de la musique joue. Donc : "Tant que la musique joue, reste bloqué dans cette boucle".   
                    pygame.time.Clock().tick(10) #permet de vérifier 10 fois que si la musique et fini
                print("Fin de la piste. Pause de 5 secondes...")
                time.sleep(5) # comme tu nous a dis Lucas attendre 5 seconde si tu veux 10 seconde on change la valeur
            except Exception as e:
                print(f"Erreur sur le fichier {musique} : {e}")
    print("--- Tout est fini ---")
if __name__ == "__main__":
    lancer_playlist()