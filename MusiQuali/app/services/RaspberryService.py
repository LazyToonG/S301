from app.DAO.RaspberryDAO import RaspberrySqliteDAO as RaspberryDAO

class RaspberryService():
    def __init__(self):
        self.rdao = RaspberryDAO()

    def montreToutRasp(self):
         return self.rdao.findAll()
    
    def ajoutR(self, identifiant, ipRasp):
	    return self.rdao.createRasp(identifiant, ipRasp)
    

        
