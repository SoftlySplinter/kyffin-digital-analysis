from gui import TextGUI, GraphGUI

def getGUI(name='text'):
	print('Using {0}-based GUI'.format(name))
	if name == 'text':
		return TextGUI() 
	if name == 'graph':
		return GraphGUI()

	return TextGUI()
