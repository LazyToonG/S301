from models import Raspberry

#à finir

def __init__(self):
		self.databasename = app.root_path + '/database.db'
		
def getDbConnection(self):
	""" connect the database and returns the connection object """
	""" connection à la base de données. Retourne l'objet connection """
	conn = sqlite3.connect(self.databasename)
	conn.row_factory = sqlite3.Row
	return conn

def findAll(self):
	""" trouve tous les pokemons """
	conn = self.getDbConnection()
	raspberry = conn.execute('SELECT * FROM raspberrys').fetchall()
	raspberry_instances = list()
	for r in raspberry:
		raspberry_instances.append(Pokemon(dict(r)))
	conn.close()
	return raspberry_instances
	
def InsertRasp(self):
    conn = self.getDbConnection()