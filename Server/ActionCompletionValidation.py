## Running a query on the server.

def runNonQuery(sql):
	from Conquest.DataAccess.Connection import ExecuteNonQuery
	return ExecuteNonQuery(sql)

def getTable(sql):
	from Conquest.DataAccess.Connection import GetRows
	return GetRows(sql)

sql = "select top 10 ActionID, ActionDescription from tblAction order by ActionID desc"
result = dict([(int(record["ActionID"]), str(record["ActionDescription"])) for record in getTable(sql)])
# >> result
# {
# 	100: "Bottle 100",
# 	99:  "Bottle 99",
# 	...
# }

rowsAffected = runNonQuery("update tblSystem set Value = '1' where Property = 'SampleProperty'")
# >> rowsAffected
# 0

## Tell the client that the process has failed with a message.
from Conquest import ErrorMessageException
raise ErrorMessageException("You cannot complete this action for reason X")