## tested on 3.0329.

## This can be used on both the client and the server

from Conquest import ErrorMessageException
IsClient = True
debug = None

def _init():
	global IsClient
	try:
		import Conquest.Silverlight
	except:
		IsClient = False
	global debug
	if IsClient:
		from System.Window.MessageBox import Show
		def _debug(o): Show(str(o))
	else:
		def _debug(o): raise ErrorMessageException(str(o))
	debug = _debug

_init()

def inspect(object):
	"""
	Shows the fields and their values for an object
	"""
	if not object:
		debug(object)
	from System.Reflection import *
	t = object.GetType()
	info = t.Name + "\n"
	meta = []
	for prop in t.GetProperties():
		meta += [{"field": prop.Name, "type": prop.PropertyType.Name, "value": str(prop.GetValue(object, None))}]
	info += "\n".join([("  {field}: {type} = {value}".format(**props)) for props in meta])
	debug(info)