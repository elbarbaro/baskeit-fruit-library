class Fruit:
	name = ''
	color = ''
	size = ''
	is_active = True

	def __init__(self, name, color, size):
		self.name = name
		self.color = color
		self.size = size

	def active(self, is_active):
		self.is_active = is_active

	def cut(self):
		if self.is_active:
			print(f'Cortando fruta: {self.name}')

	def __str__(self):
		return f'name: {self.name}, color: {self.color}, size {self.size}'


class Basket:
	fruits = None
	is_active = False


	def active(self):
		self.is_active = True
		self.fruits = []


	def add(self, fruit):
		if self.is_active:
			fruits.append(fruit)

	def show(self):
		if self.is_active:
			for friut in fruits:
				print(f'Fruta {fruit}')
				fruit.cut()


