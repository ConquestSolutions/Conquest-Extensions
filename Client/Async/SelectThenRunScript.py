def done(): callBack(None)
def fail(s): callBack(s)
def debug(*obs):
	from System.Windows.MessageBox import Show
	Show("\n".join([ str(ob) for ob in obs]))

def prepareSql(sql, **kw):
	import re
	return re.sub("\s*\| ", "\n", sql).strip().format(**kw).replace("\n", " ")

from Conquest.Silverlight import App

def selectThenExecuteMany():
	# 1
	def onSelected(records):
		if len(records) == 0: done()
		script = ""
		for record in records:
			record.ActionID
			script += """
			| update tblAction set ActionDescription = ActionDescription where ActionID = {id};
			| update tblAction set ActionDescription = ActionDescription where ActionID = {id};
			| update tblAction set ActionDescription = ActionDescription where ActionID = {id};
			"""
		script = prepareSql(script, id = record.ActionID)
		debug(script)
		App.ExecuteNoQuery(script, onUpdated)

	# 2
	def onUpdated(rowsAffected):
		debug("rowsAffected should be 9, actual: " + str(rowsAffected))
		done()

	App.RunQuery("select top 3 ActionID from tblAction", onSelected)

isWaitCallBack = True
selectThenExecuteMany()
