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
				elif self.dataType in ['rgb', 'hsv']:
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
                elif self.dataType in ['rgb', 'hsv']:
			self.renderGraph(data)
		elif self.dataType == 'default':
			print 'Nothing to do.'
                else:
			raise Exception('Type "{0}" unknown.'.format(self.dataType.format(self.dataType)))

	def renderGraph(self, data):
		gR = []
		gG = []
		gB = []
		years = []
		for key in sorted(data.keys()):
			mR, mG, mB = 0,0,0
			try:
				year = int(key)
				years.append(year)
			except ValueError:
				continue
			for ((r,g,b,a),(x)) in data[key]:
				mR += r
				mG += g
				mB += b
			gR.append(mR / len(data[key]))
			gG.append(mG / len(data[key]))
			gB.append(mB / len(data[key]))
		r = plot.plot(years, gR, 'c', label='Hue')
		g = plot.plot(years, gG, 'm', label='Saturation')
		b = plot.plot(years, gB, 'y', label='Value')

		plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

		plot.xlabel('Year')
		plot.ylabel('Value')
		plot.show()
		

	def renderHist(self, data):
		for key in sorted(data.keys()):
			for value in data[key]:
				self.renderIndividualHist(key, value)

	def renderIndividualHist(self, key, data):
		height = 500
		width = 500
		(r,g,b) = cv.GetDims(data.bins)

		(_,tallest,_,_) = cv.GetMinMaxHistValue(data)
		scale = height/tallest
		if scale > 1:
			scale = 1

		histImage = cv.CreateImage((width,height), 8, 3)
		prev = -1

		cv.Rectangle(histImage, (0,0), (width, height), cv.CV_RGB(0,0,0), cv.CV_FILLED)

		step = width/(r*g*b)
		cur = 0
		for (i,j,k) in iter3D(range(r), range(g), range(b)):
			intensity = cv.QueryHistValue_3D(data, i, j, k)
			color = cv.CV_RGB(int((255/r)*i), int((255/g)*j), int((255/b)*k))
			x1 = cur
			cur+=step
			x2 = x1 + step 
			cv.Rectangle(histImage, (int(x1), height), (int(x2), height - int(intensity * scale)), color, cv.CV_FILLED)

		cv.NamedWindow("Histogram")
		cv.ShowImage("Histogram", histImage)
		cv.WaitKey(0)



def iter3D(aList, bList, cList):
	for a in range(len(aList)):
		for b in range(len(bList)):
			for c in range(len(cList)):
				yield(aList[a], bList[b], cList[c])
