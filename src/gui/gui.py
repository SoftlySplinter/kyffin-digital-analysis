import matplotlib.pyplot as plot
import mpl_toolkits.mplot3d.axes3d as p3d
import cv
import sys

class GUI:
	def __init__(self, dataType='default'):
		self.dataType = dataType
	def render(self, data, dataType='default'):
		raise NotImplementedError('Should be implemented in sub-classes')

class TextGUI(GUI):
	def render(self, data):
		print self.dataType
                for key in sorted(data.keys()):
                        for value in data[key]:
	        	        if self.dataType == 'histogram':
       		         		self.renderHistogram(value)
				elif self.dataType == 'rgb':
					print '{0}: {1}\n'.format(key, value)
				elif self.dataType == 'default':
					print 'Nothing to do.'
				else:
					raise Exception( 'No type specified')

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
		if self.dataType == 'histogram':
			self.renderHist(data)
                elif self.dataType == 'rgb':
			self.renderGraph(data)
		elif self.dataType == 'default':
			print 'Nothing to do.'
                else:
			raise Exception('Type "{0}" unknown.'.format(self.dataType.format(self.dataType)))

	def renderGraph(self, data):
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
		

	def renderHist(self, data):
		for key in sorted(data.keys()):
			for value in data[key]:
				self.renderIndividualHist(key, value)

	def renderIndividualHist(self, key, data):
#		cv.NormalizeHist(data, 255.0)
#		cv.ThreshHist(data, 0.1)

		(r,g,b) = cv.GetDims(data.bins)
		height = 500
		width = 500
		histImage = cv.CreateImage((width,height), 8, 3)
		prev = -1

		rvals = []
		for i in range(r):
			val = cv.QueryHistValue_3D(data, i, 0, 0)
			rvals.append(val)
	
		gvals = []
		for i in range(g):
			val = cv.QueryHistValue_3D(data, 0, i, 0)
			gvals.append(val)
		
		bvals = []
		for i in range(b):
			val = cv.QueryHistValue_3D(data, 0, 0, i)
			bvals.append(val)
		plot.hist(rvals, r, histtype='barstacked', color='r')

		plot.xlabel('Bin')
		plot.ylabel('Intensity')

		plot.title(key)

		plot.show()
