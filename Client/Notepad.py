def Notepad(file, text):
	"""
	Writes a file to the user's documents directory then opens it with notepad
	Requires Elevated Privileges. Elevated Privileges works best in IE.
	"""
	from System import Environment
	from System.IO import File, FileMode, Path
	from System.Runtime.InteropServices.Automation import AutomationFactory

	file = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments),"USERPROFILE")
	File.WriteAllText(file, text)

	cmd = AutomationFactory.CreateObject("WScript.Shell");
	cmd.Run("notepad.exe " + file);
	
Notepad("test.txt", "hello")