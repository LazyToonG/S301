from app.DAO.RaspberryDAO import RaspberrySqliteDAO as RaspberryDAO
import time, subprocess

class RaspberryService():
    def __init__(self):
        self.rdao = RaspberryDAO()

    def montreToutRasp(self):
         return self.rdao.findAll()
    
    def ajoutR(self, identifiant, ipRasp):
        return self.rdao.createRasp(identifiant, ipRasp)
    
    def selectRIp(self, ipRasp):
        r = self.rdao.findByIp(ipRasp)
        if r:
            return r  # retourne une string
        return None

    def selectRNom(self, nom):
        r = self.rdao.findByNom(nom)
        if r:
            return r  # retourne une string
        return None
    
    def supprimeR(self, ipRasp):
        return self.rdao.deleteRasp(ipRasp)
    
    def verifieShellRasp(self):
        return self.rdao.verifieShell()
    
    def envoieChaqueChangementPlanning(self):
        time.sleep(10)  # Attendre 10 secondes avant d'exécuter la fonction pour s'assurer que le fichier est complètement sauvegardé
        raspberrys = self.rdao.findAll()
        for r in raspberrys:
            if r["ipRasp"] is None or r["nom"] is None:
                continue  # Ignorer les entrées avec des informations incomplètes
            subprocess.run(["rsync", "-avz", "--delete", "-e", "ssh","./app/static/rasdata/",  f"{r['nom']}@{r['ipRasp']}:/home/{r['nom']}/musiquali/"])
            time.sleep(5)
            subprocess.run(["ssh", f"{r['nom']}@{r['ipRasp']}", "python3", f"/home/{r['nom']}/musiquali/RAS.py"])

        
    # def envoieDossierMusique(self):
        
    
        
