from objects import cars
from cars import example
from example import CARLIST

key_stmt          = []
safe_stmt         = []

def define_dbstmt():
	"""
	Database statement definitions
	"""
	key_stmt.iff  = ["IF EXISTS "]
	key_stmt.drop = ["DROP TABLE "]
	key_stmt.make = ["CREATE TABLE "]
	key_stmt.insert = ["INSERT INTO "]
	key_stmt.select = ["SELECT "]

class PyDbTest():
	"""
	Checks the id()
	"""
	safe_id = []
	cars    = CARLIST
	def __init__(self, car):
		super(P, self).__init__()
		self.car = car
	def valid_set(cars):
		for car in cars:
			safe_id[car] = car.id()
		pass

	def __isset__(self):
		return safe_id

	def check_list(CarList):
		pass