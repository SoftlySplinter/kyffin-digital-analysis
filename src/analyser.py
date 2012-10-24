#! /usr/bin/env python

import cv
import numpy
import csv
import matplotlib.pyplot as plot

DATA_DIR = 'data/'

class Analyser:
	def __init__(self, technique):
		self.technique = technique

	def analyse(self, data):
		'''Analyse a CSV file which contains the data for a set of images'''
		averages = dict()
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

		averaged = dict()

		x = []
		yR = []
		yG = []
		yB = []

		for (k,v) in averages.items():
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

		plot.plot(x,yR,'rx',x,yG,'gx',x,yB,'bx')
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

