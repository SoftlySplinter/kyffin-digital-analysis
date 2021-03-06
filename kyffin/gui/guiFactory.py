from gui import GUI, TextGUI, GraphGUI

def getGUI(name='text', dataType='default'):
	if name == 'text':
		return TextGUI(dataType) 
	if name == 'graph':
		return GraphGUI(dataType)

	return GUI(dataType)
