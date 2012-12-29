import matplotlib.pyplot as plot
import mpl_toolkits.mplot3d.axes3d as p3d
import cv
import sys

class GUI:
	def __init__(self, dataType='default'):
		self.dataType = dataType
	def render(self, data, dataType='default'):
		pass

class TextGUI(GUI):
	def render(self, paintings):
		print self.dataType
		for painting in paintings:
			print '{0} ({1}): {2}'.format(painting.title, painting.year, painting.data)

class GraphGUI(GUI):
	def render(self, data):
		if self.dataType == 'histogram':
			self.renderHist(data)
                elif self.dataType == 'rgb':
			self.renderGraph(data, ['Red','Green','Blue'], ['r-','g-','b-'])
		elif self.dataType == 'hsv':
			self.renderGraph(data, ['Hue','Saturation','Value'], ['c-','m-','y-'])
		elif self.dataType == 'edge-orientation':
			for painting in data:
				cv.ShowImage(painting.title, painting.data)
				cv.WaitKey(0)
		elif self.dataType == 'default':
			print 'Nothing to do.'
                else:
			raise Exception('Type "{0}" unknown.'.format(self.dataType.format(self.dataType)))

	def renderGraph(self, data, legend, lineType):
		v1 = []
		v2 = []
		v3 = []
		years = []

		data.sort(key = lambda x: int(x.year))
		for painting in data:
			((a,b,c,_),_) = painting.data
			
			v1.append(a)
			v2.append(b)
			v3.append(c)
			years.append(painting.year)

		plot.figure(1)
		p1, = plot.plot(years, v1, lineType[0])
		p2, = plot.plot(years, v2, lineType[1])
		p3, = plot.plot(years, v3, lineType[2])
		plot.legend([p1,p2,p3], legend, loc=2)
		plot.xlabel('Year')
		plot.ylabel('Value')
		
		
		plot.show
		

	def renderHist(self, data):
		for painting in data:
			if painting.data is None:
				continue
			self.renderIndividualHist(painting)

	def renderIndividualHist(self, painting):
		height = 500
		width = 500
		(r,g,b) = cv.GetDims(painting.data.bins)

		(_,tallest,_,_) = cv.GetMinMaxHistValue(painting.data)
		scale = height/tallest
		if scale > 1:
			scale = 1

		histImage = cv.CreateImage((width,height), 8, 3)
		prev = -1

		cv.Rectangle(histImage, (0,0), (width, height), cv.CV_RGB(0,0,0), cv.CV_FILLED)

		step = width/(r*g*b)
		cur = 0
		for (i,j,k) in iter3D(range(r), range(g), range(b)):
			intensity = cv.QueryHistValue_3D(painting.data, i, j, k)
			color = cv.CV_RGB(int((255/r)*i), int((255/g)*j), int((255/b)*k))
			x1 = cur
			cur+=step
			x2 = x1 + step 
			cv.Rectangle(histImage, (int(x1), height), (int(x2), height - int(intensity * scale)), color, cv.CV_FILLED)

		windowTitle = '{0} ({1})'.format(painting.title, painting.year)
		cv.NamedWindow(windowTitle)
		cv.ShowImage(windowTitle, histImage)
		cv.WaitKey(0)



def iter3D(aList, bList, cList):
	for a in range(len(aList)):
		for b in range(len(bList)):
			for c in range(len(cList)):
				yield(aList[a], bList[b], cList[c])
