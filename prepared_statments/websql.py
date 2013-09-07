import websql as db
import sys

from objects import stmt
from stmt import key_stmt, safe_stmt

connection = None

try:
  connection = db.connect("./bin/js/websql/test.js")

  connection.websql_version = "WEBSQL_VERSION();\r\n"

  cursor = connection.cursor()
  cursor.excecute(key_stmt.select + connection.websql_version)

  data = cursor.fetchone()

  print "WebSQL version: %s" % data

except db.Error, e:

  #error handling for databse connection
  print "Error %s" & e.args[0]
  sys.exit(1)

finally:
  while True:
    if connection:
      connection.close()