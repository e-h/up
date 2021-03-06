import websql as db
import sys

connection = db.connect("objects/cars/example.py")

from objects import cars, stmt
from cars import example
from example import Car, CARLIST

test = CARLIST

from stmt import key_stmt, safe_stmt

def connect_toworld(PyDbTest):
  """Environment for insertion"""
  with online:
    MyRDB = ['db':{label, set_table}]
    MyRDB.label = 'Cars'
    MyRDB.set_table = ["Cars(Id INT, Name TEXT, Price INT);\n"]

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

  # iterate through cars
  for car in test:
    cursor.excecute(key_stmt.insert + MyRDB.label + (car as Car))