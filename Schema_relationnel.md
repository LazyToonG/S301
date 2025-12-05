# Schema_relationnel.md

- ---------------
- Utilisateurs (<ins>int idUtilisateur</ins>, str nom, str mdp, str role, int idEntreprise) où idEntreprise est une clé étrangère renvoyant à la table Entreprise
- ---------------
- Musique (<ins>int idMusique</ins>, int idPlaylist, str nomMusique, str genre, str lien, str auteur, int durée) où idPlaylist est une clé étrangère renvoyant à la table Playlist
- - ---------------
- Messages (<ins>int idMessage</ins>, str theme, str idEntreprise) où idEntreprise est une clé étrangère renvoyant à la table Entreprise
- - ---------------
- Entreprise (<ins>int idEntreprise</ins>, str nomEntreprise, str type, str lieu)
- - ---------------
- Playlist (<ins>int idPlaylist</ins>, int idMusique, int idEntreprise) où la clé idEntreprise est une clé étrangère renvoyant à la table Entreprise
- - ---------------
- Logs (<ins>int idLogs</ins>, int IdEntreprise, int idPlaylist) où idEntreprise est une clé étrangère renvoyant à la table Entreprise et idPlaylist renvoyant à la table Playlist
- - ---------------

