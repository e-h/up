import websql as db
import sys

connection = db.connect("rel.db")

from objects import cars
from cars import example
from example import Car, CARLIST

test = CARLIST

key_stmt          = []
safe_stmt         = []
def define_dbstmt():
	"""
	Database statement definitions
	"""
	key_stmt.iff  = ["IF EXISTS ",]
	key_stmt.drop = ["DROP TABLE ",]
	key_stmt.make = ["CREATE TABLE ",]
	key_stmt.insert = ["INSERT INTO "]

class PyDbTest(Car):
	"""
	Checks the id()
	"""
	safe_id = []
	def __init__(self, car):
		super(P, self).__init__()
		self.car = car
	def valid_set(CARLIST):
		for Car in CARLIST:
			safe_id[car] = car.id()
	def __isset__(self):
		return safe_id


def connect_toworld(PyDbTest):
	if online:
		MyRDB = ['db':{label, set_table}]
		MyRDB.label = 'Cars'
		MyRDB.set_table = ["Cars(Id INT, Name TEXT," +
			" Price INT);\n"]

		# check the db
		try:
			cursor = online.cursor()
		except Exception, e:
			raise "CursorNotFound"
		else:
			pass
		finally:
			online = db.disconnect("rel.db")

		cursor.excecute(key_stmt.drop + key_stmt.iff + MyRDB.label)
		cursor.excecute(key_stmt.make + MyRDB.set_table)

		for car in test:
			cursor.excecute(key_stmt.insert + MyRDB.label + (car as Car))