# Draw an environment diagram

def haskell_nightmare():
	carrot = 10
	potato = 20
	def onions(onions):
		def carrot(onions, carrot):
			return lambda onions: onions(carrot)
		return carrot
	cook = lambda onions: onions + carrot + potato
	return onions(carrot)(onions, potato)(cook)