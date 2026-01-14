import sqlite3
from app import app
from app.models.Raspberry import Raspberry

#à finir
class RaspberrySqliteDAO():

	def __init__(self):
			self.databasename = app.root_path + 'static/data//database.db'
			self._initTable()
			
	def getDbConnection(self):
		""" connect the database and returns the connection object """
		""" connection à la base de données. Retourne l'objet connection """
		conn = sqlite3.connect(self.databasename)
		conn.row_factory = sqlite3.Row
		return conn
	
	def _initTable(self):
		conn = self._getDbConnection()
		conn.execute('''
			CREATE TABLE IF NOT EXISTS raspberry (
				identifiant TEXT NOT NULL DEFAULT 'raspberry',
				ipRasp TEXT PRIMARY KEY 
			)
		''')
		conn.commit()
		conn.close()

	def findAll(self):
		""" trouve tous les raspberry """
		conn = self.getDbConnection()
		raspberry = conn.execute('SELECT * FROM raspberrys').fetchall()
		raspberry_instances = list()
		for r in raspberry:
			raspberry_instances.append(Raspberry(dict(r)))
		conn.close()
		return raspberry_instances
		
	def createRasp(self, identifiant, ipRasp):
		conn = self._getDbConnection()
		try:
			conn.execute(
				"INSERT INTO raspberry (identifiant, ipRasp) VALUES (:identifiant, :ipRasp)",
				{"identifiant":identifiant, "ipRasp":ipRasp}
			)
			conn.commit()
			return True
		except Exception:
			return False
		finally:
			conn.close()