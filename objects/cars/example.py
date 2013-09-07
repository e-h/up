def sub_init(self, id, *args, **kwargs):
	pass

class CarMeta(type):
	"""
	def __new__(class Car(object):
		def __init__(self, arg):
			super(Car, self).__init__()
			self.arg = arg
			), 'Car', bases, attributes)
	"""
	def __new__(cls, name, bases, attrs):
		attrs['__init__'] = sub_init
		return super(CarMeta, cls).__new__(cls, name, bases, attrs)

class Car(object):
	"""Defintion for database"""
	__metaclass__ = CarMeta

	def __init__(self, id, name, price):
		self.data = [self.id, self.name, self.price]

CARLIST = {'first':[1, 'Audi', 52642],
		   'second':[2, 'Mercedes', 57127],
		   'third':[3, 'Skoda', 9000],
		   'fourth':[4, 'Volvo', 29000],
		   'fifth':[5, 'Bently', 350000],
		   'sixth':[6, 'Citroen', 21000],
		   'seventh':[7, 'Hummer', 41400],
		   'eight':[8, 'Volkswagen', 21600],
		   #'Name':[:len()],'':[],}
		   }