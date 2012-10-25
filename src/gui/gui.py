class GUI:
	def render(self, data):
		raise NotImplementedError('Should be implemented in sub-classes')

class TextGUI(GUI):
	def render(self, data):
		for key in sorted(data.keys()):
			print '{0}: {1}\n'.format(key, data[key])

class GraphGUI(GUI):
	def render(self, data):
		print 'To Do.'
