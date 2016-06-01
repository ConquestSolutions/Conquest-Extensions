def liftCB(transform):
	"""
	Takes a callback that receives a value of type B
		B => ()
	Wraps a function that transforms A to B
		A => B
	And returns a callback that receives a type A
		A => ()

	Usage:
		receivesA = liftCB(transform)(receiveB)
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