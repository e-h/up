import urllib2
import json as simplejson
import random
import websql as db

from objects import foods
from foods import productInfo

productIds = []
apiKeys = ["ef236b29aaf1de879f1167a295b36ddb"]

file = open("productIds3.txt", "r")
for line in file:
  productIds.append(line.strip())
print productIds
file.close()

connection = db.connect("productInfo.db")

from stmt import key_stmt, safe_stmt

with connection:

  cursor = connection.cursor()
  cursor.execute(key_stmt.drop + key_stmt.iff + productInfo.__name__())