def done(): callBack(None)
def fail(s): callBack(s)
def debug(*obs):
	from System.Windows.MessageBox import Show
	Show("\n".join([ str(ob) for ob in obs]))

def stripMargin(s):
	import re
	return re.sub("\s*\| ", "\n", s).strip()

def runQuery(sql, f):
	from Conquest.Silverlight import App
	formattedSql = stripMargin(sql).replace("\n", " ")
	App.RunQuery(formattedSql, f)

## How to run a query before saving.

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
	checkSql = """
	| select ActionID from tblAction where (StdActionID is null or StdActionID <= 0 or StdActionID > 0 and StdActionID = {sid})
	| and ActionID = {aid};
	""".format(
		sid=str(source.StdActionID or 0), 
		aid=str(source.ActionID))
	runQuery(checkSql, onResult)
	
## The validation uses a callback, so we must set this flag to True

isWaitCallBack = True
databaseCheckBeforeSave()