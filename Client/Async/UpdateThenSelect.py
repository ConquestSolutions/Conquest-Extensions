def done(): callBack(None)
def fail(s): callBack(s)
def debug(*obs):
	from System.Windows.MessageBox import Show
	Show("\n".join([ str(ob) for ob in obs]))

from Conquest.Silverlight import App

def updateThenSelect():
	if source.ActionID <= 0:
		return done()

	# 1
	def onUpdated(i):
		App.RunQuery("select ActionDescription from tblAction where ActionID = {id}".format(
			id = source.ActionID), 
		onSelected)
    
    # 2
	def onSelected(records):
		debug(records[0].ActionDescription)
		done()

	App.ExecuteNoQuery(
		"update tblAction set ActionDescription = '{desc}' where ActionID = {id}".format(
			desc = source.ActionDescription + "*", 
			id = source.ActionID), onUpdated)

isWaitCallBack = True
updateThenSelect()