class Plov():
    def __init__(self, plov_type, name='Плов', rice=True, meat=True):
        self.plov_type = plov_type
        self.name = name
        self.rice = rice
        self.meat = meat

    def get_portion(self):
    	print(f'1 portion of {self.plov_type} {self.name} is ready!')

    def add_carrot(self):
    	print(f'carrot added to the {name}')


class Uzbek_Plov(Plov):
	def __init__(self, plov_type, name='Плов', rice=True, meat=True):
		self.plov_type = plov_type
		self.name = name
		self.rice = rice
		self.meat = meat

	def add_carrot(self):
		print(f'No carrot in {self.plov_type} {self.name}')