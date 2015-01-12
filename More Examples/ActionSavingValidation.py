def done(): callBack(None)
def fail(s): callBack(s)
def stripMargin(s):
	import re
	return re.sub("\s*\| ", "\n", s).strip()
def prepareSql(sql):
	return stripMargin(sql).replace("\n", " ")
def debug(*obs):
	from System.Windows.MessageBox import Show
	Show("\n".join([ str(ob) for ob in obs]))

## How to run a query before saving.

from Conquest.Silverlight import App
def databaseCheckBeforeSave():
	"""
	Make sure the action is not re-assigned to another standard action, once assigned.
	"""
	if source.ActionID <= 0:
		return done()
	def onResult(collection):
		if collection == None or len(collection) != 1:
			return fail("You cannot change the Standard Action once assigned.")
		done()
	checkSql = prepareSql("""
	| select ActionID from tblAction where (StdActionID is null or StdActionID <= 0 or StdActionID > 0 and StdActionID = %s)
	| and ActionID = %s;
	""" % (str(source.StdActionID or 0), str(source.ActionID)))
	debug(checkSql)
	App.RunQuery(checkSql, onResult)
	
## The validation uses a callback, so we must set this flag to True

isWaitCallBack = True
databaseCheckBeforeSave()