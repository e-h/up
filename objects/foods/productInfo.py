def sub_init(self, id, *args, **kwargs):
	"""
	@originalauthor::=> stackoverflow answer
	"""
	pass

class PrdouctInfoMeta(type):
	"""
	Meta class for product info
	"""
	def __new__(cls, name, bases, attrs):
		attrs['__init__'] = sub_init
		return super(PrdouctInfoMeta, cls).__new__(cls, name, bases, attrs)
	# add name meta decorator

class ProductInfo(object):
	"""class definition for ProductInfo"""
	def __init__(self, infos):
		super(ProductInfo, self).__init__()
		self.infos = infos
	def __name__(self):
		return self.__name__
	infos = ['product_id':{"INT"}, 'product_name':{"TEXT"},
			'ingredients': {"TEXT"}, 'serving_size': {"TEXT"},
			'calories': {"INT"}, 'total_fag_g': {"INT"},
			'fat_trans_g': {"INT"}, 'fat_trans_percent': {"INT"},
			'cholesterol_mg': {"INT"}, 'sodium_mg': {"INT"},
			'sodium_percent': {"INT"}, 'carbo_g': {"INT"},
			'carbo_percent': {"INT"}, 'carbo_fibre_g': {"INT"},
			'carbo_fibre_percent': {"INT"},
			'carbo_sugars_g': {"INT"},
			'protein_g': {"INT"}, 'vitamin_a_percent': {"INT"},
			'iron_percent': {"INT"}, 'micro_nutrients':{"TEXT"},
			'tips': {"TEXT"}, 'diet_id': {"INT"}, 'diet_type': {
			"TEXT"
			}]
