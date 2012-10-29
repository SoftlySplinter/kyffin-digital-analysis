import matplotlib.pyplot as plot
import mpl_toolkits.mplot3d.axes3d as p3d
import cv
import sys

class GUI:
	def render(self, data):
		raise NotImplementedError('Should be implemented in sub-classes')

class TextGUI(GUI):
	def render(self, data):
                for key in sorted(data.keys()):
                        for value in data[key]:
	        	        if hasattr(value, 'bins'):
       		         		self.renderHistogram(value)
				else:
					print '{0}: {1}\n'.format(key, value)

	def renderHistogram(self, data):
                (r,g,b) = cv.GetDims(data.bins)
                for rN in range(r):
			for gN in range(g):
				for bN in range(b):
					print(cv.QueryHistValue_3D(data, rN, gN, bN)),
				print ''
			print '\n'

class GraphGUI(GUI):
	def render(self, data):
		gR = []
		gG = []
		gB = []
		for key in sorted(data.keys()):
			mR, mG, mB = 0,0,0
			for ((r,g,b,a),(x)) in data[key]:
				mR += r
				mG += g
				mB += b
			gR.append(mR / len(data[key]))
			gG.append(mG / len(data[key]))
			gB.append(mB / len(data[key]))
		fig = plot.figure()
		axes = p3d.Axes3D(fig)
		axes.scatter(gR,gG,gB)
		
		plot.show()		
