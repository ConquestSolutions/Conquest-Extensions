from Conquest.Silverlight import DataGridSelectorDialog, DataGridDataSourceArgs, MessagePop
from System.Windows.Controls import Button, StackPanel
from System import String, Array

sql = "select top 100 ActionID, ActionDescription from tblAction order by ActionID desc"
dialog = DataGridSelectorDialog()
dialog.Header = "100 Recent actions"
dialog.DataSource = DataGridDataSourceArgs(sql)

# Show an export button
dialog.CanExport = True

# If False single rows can be selected, If None selection is disabled
dialog.CanSelectMany = True

# If a list of action names are defined, they will appear as buttons
# in the dialog
dialog.Actions = Array[String](["Do A", "Do B"])

def dialog_Closed(s,e):
	if dialog.DataSource.HasNoResult:
		MessagePop.Show("No Recent Actions.")
	elif dialog.DataSource.Error != None:
		raise dialog.Error
	elif (dialog.SelectedAction != None):
		MessagePop.Show(
		"Action   : " + dialog.SelectedAction + "\n\n" +
		"Selection: " + String.Join(",", [record.ActionID.ToString() for record in dialog.SelectedItems]))

dialog.Closed += dialog_Closed
dialog.Show()