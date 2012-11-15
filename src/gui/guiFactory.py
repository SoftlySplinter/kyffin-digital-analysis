from gui import GUI, TextGUI, GraphGUI

def getGUI(name='text', dataType='default'):
	print('Using {0}-based GUI'.format(name))
	if name == 'text':
		return TextGUI(dataType) 
	if name == 'graph':
		return GraphGUI(dataType)

	return GUI(dataType)
