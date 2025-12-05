# Schema_relationnel.md

- Utilisateurs ( ++int idUtilisateur++ , str nom, str mdp, str role, int idEntreprise) où idEntreprise est une clé étrangère renvoyant à la table Entreprise
- Musique (int idMusique, int idPlaylist, str nomMusique, str genre, str lien, str auteur, int durée) où idPlaylist est une clé étrangère renvoyant à la table Playlist
- Messages (int idMessage, str theme, str idEntreprise) où idEntreprise est une clé étrangère renvoyant à la table Entreprise
- Entreprise (int idEntreprise, str nomEntreprise, str type, str lieu)
- Playlist (int idPlaylist, int idMusique, int idEntreprise) où la clé idEntreprise est une clé étrangère renvoyant à la table Entreprise
- Logs (int idLogs, int IdEntreprise, int idPlaylist) où idEntreprise est une clé étrangère renvoyant à la table Entreprise et idPlaylist renvoyant à la table Playlist

- Voici un mot <u>souligné</u> dans une phrase.
