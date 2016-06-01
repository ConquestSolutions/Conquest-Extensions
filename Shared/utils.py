def liftCB(transform):
	"""
	Takes a callback that recieves a value of type A
		A => ()
	Wraps a function that transforms A to B
		A => B
	And returns a callback that recieves a type B
		B -> ()

	Usage:
		recievesA = liftCB(transform)(recievesB)
	"""
	def wrap(receive):
		def apply(*value):
			result = transform(*value)
			if not hasattr(result, "__len__"):
				result = [result]
			receive(*result)
		setattr(apply, "__name__", transform.__name__ + "Callback") # for debugging
		return apply
	return wrap