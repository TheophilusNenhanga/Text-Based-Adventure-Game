class Enchantment:
	def __init__(self):
		self.name = "Enchantment"
		self.level = 0
		self.type_affect = "normal"
		self.description = """
				A magical spell embedded into your weapon.
					This might just come in handy.
		"""
		self.value = 0

	def __str__(self):
		return self.name

	def damage_multiplier(self):
		if self.level == 0:
			damage_multiplier = 0
			return damage_multiplier
		if self.level == 1:
			damage_multiplier = 1.5
			return damage_multiplier
		if self.level == 2:
			damage_multiplier = 2
			return damage_multiplier
		else:
			damage_multiplier = 1.25
			return damage_multiplier


class Hydration(Enchantment):
	def __init__(self):
		super().__init__()
		self.name = "Hydration"
		self.level = 1
		self.type_affect = "rock"
		self.description = """
					This enchantment hydrates all it touches.
						I wonder what happens to a wet rock?
		"""
		self.value = 100


class Dehydration(Enchantment):
	def __init__(self):
		super().__init__()
		self.name = "Dehydration"
		self.level = 1
		self.type_affect = "water"
		self.description = """
					This enchantment dehydrates all it touches.
						I wonder what happens to dry water?
		"""
		self.value = 100
