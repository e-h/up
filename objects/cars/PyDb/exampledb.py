"""
html5rocks.webdb.open = function() {
  var dbSize = 5 * 1024 * 1024; // 5MB
  html5rocks.webdb.db = openDatabase("Todo", "1.0", "Todo manager", dbSize);
}

html5rocks.webdb.onError = function(tx, e) {
  alert("There has been an error: " + e.message);
}

html5rocks.webdb.onSuccess = function(tx, r) {
  // re-render the data.
  // loadTodoItems is defined in Step 4a
  html5rocks.webdb.getAllTodoItems(loadTodoItems);
}"""
# WebSQL API via Python
cars.example.padded.db = None

cars.example.padded.open = def function():
	pass

class RenderHtml5WebSQL:
	pass

cars.example.padded.db = RenderHtml5WebSQL()

RenderHtml5WebSQL.open = def __open__(self):
	pass

class RenderDb(RenderHtml5WebSQL):
	def __init__(self, iterable):
		self.cars_list = []
		self.__update(iterable)#pydoc
	def __open__(self):
		RenderHtml5WebSQL.open.dbSize = math.pow(2, 23)
		RenderHtml5WebSQL.db = openDatabase("Cars", "0.1", "Example WebDb")
	def onError(tx, e):
		print "THere has been an error: " + e.message
	def onSuccess(tx, r):
		RenderHtml5WebSQL.getAllCarItems(loadCarItems)
