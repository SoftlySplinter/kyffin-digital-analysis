import cv

class EdgeOrientation(Technique):
	DEFAULT = 'sobel'
	def __init__(self, algorithm=EdgeOrientation.DEFAULT):
		self.algorithm = algorithm

	def Analyse(self, painting):
		print 'TODO'

	def distance(self, a, b):
		return 0
		
