from objects/cars/example import Car, CARLIST

key_stmt          = []
safe_stmt         = []

class Statement():
  """Define inputs for queries"""
  def __init__(self):
  	"""Removes any existing def'n"""
    if key_stmt:
      key_stmt = None
    elif safe_stmt:
      safe_stmt = None
    key_stmt, safe_stmt = []
  def define_dbstmt():
    """Database statement definitions"""
    key_stmt.iff  = ["IF EXISTS "]
    key_stmt.drop = ["DROP TABLE "]
    key_stmt.make = ["CREATE TABLE "]
    key_stmt.insert = ["INSERT INTO "]
    key_stmt.select = ["SELECT "]

class PyDbTest():
  """
  Checks the id() before insertion
  """
  safe_id = []
  cars    = CARLIST
  define_dbstmt()
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
    for car in CarList:
      if safe_id[car] is CarList[car].id():
        pass
      elif safe_id[car] is not CarList[car].id():
        return False
    return True
  #pass

#add meta