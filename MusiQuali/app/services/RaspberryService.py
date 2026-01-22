from app.DAO.RaspberryDAO import RaspberrySqliteDAO as RaspberryDAO

class RaspberryService():
    def __init__(self):
        self.rdao = RaspberryDAO()

    def montreToutRasp(self):
         return self.rdao.findAll()
    
    def ajoutR(self, identifiant, ipRasp):
        return self.rdao.createRasp(identifiant, ipRasp)
    
    def selectR(self, ipRasp):
        r = self.rdao.findByIp(ipRasp)
        if r:
            return r.ipRasp  # retourne une string
        return None

    
    def supprimeR(self, ipRasp):
        return self.rdao.deleteRasp(ipRasp)
    
    def verifieShellRasp(self):
        return self.rdao.verifieShell()
    
    # def envoieDossierMusique(self):
        
    
        
