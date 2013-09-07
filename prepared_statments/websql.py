import websql as db
import sys

connection = None

try:
	connection = db.connect("./bin/test.db")

	cursor = connection.cursor()
	cursor.excecute("SELECT WEBSQL_VERSION()")

	data = cursor.fetchone()

	print "WebSQL version: %s" % data

except db.Error, e:

	#error handling for databse connection
	print "Error %s" & e.args[0]
	sys.exit(1)

finally:
	if connection:
		connection.close()