from gui import TextGUI

def getGUI(name='text'):
	print('Using {0}-based GUI'.format(name))
	if name is 'text':
		return TextGUI() 
	if name is 'graph':
		return GraphGUI()

	return TextGUI()
