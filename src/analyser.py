#! /usr/bin/env python

import cv
import numpy
import csv
import matplotlib.pyplot as plot
import mpl_toolkits.mplot3d.axes3d as p3d

DATA_DIR = 'data/'

class Analyser:
	def __init__(self, technique):
		self.technique = technique

	

	def analyse(self, data):
		'''Analyse a CSV file which contains the data for a set of images'''
		averages = {}
		with open (data, 'r') as csvFile:
			dataReader = csv.reader(csvFile, delimiter=',', quotechar='"')
			for row in dataReader:
				avg = self.analyseRow(row)
				if avg is None:
					continue
				if row[1] not in averages:
					averages[row[1]] = [avg]
				else:
					averages[row[1]].append(avg)

		averaged = {}

		x = []
		yR = []
		yG = []
		yB = []

		keys = averages.keys()
		keys = sorted(keys)

		for k in keys:
			v = averages[k]


			mR = 0
			mG = 0
			mB = 0
			for ((r,g,b,i), std) in v:
				mR += r
				mG += g
				mB += b
			mR /= len(v)
			mG /= len(v)
			mB /= len(v)
		
			try :	
				x.append(int(k))
			except BaseException:
				continue
			yR.append(mR)
			yG.append(mG)
			yB.append(mB)

		fig = plot.figure()
		ax = p3d.Axes3D(fig)
		ax.scatter(yR, yG, yB)

#		plot.plot(x,yR,'r-',x,yG,'g-',x,yB,'b-')
		plot.show()

	def analyseRow(self, row):
		'''Analyse a row in the CSV file.
		The format of these fils is as follows:
	
		0) Title
		1) Year
		2) Type
		3) Collection
		4) File'''
		try:
			image = cv.LoadImageM(DATA_DIR + row[4])
			return self.technique.Analyse(image)
		except IOError:
			return None

if __name__ == '__main__':
	raise ImportWarning('Intended as a library, not as a main class.')

