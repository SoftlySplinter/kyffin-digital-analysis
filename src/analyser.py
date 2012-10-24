#! /usr/bin/env python

import cv
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
		rY = []
		bY = []
		gY = []
		x = []
		for (k,v) in averages.items():
			for ((r,g,b,i), std) in v:
				try:
					year = int(k)
					x.append(year)
					rY.append(r)
					bY.append(b)
					gY.append(g)
				except BaseException as e:
					continue
		plot.plot(x,rY,'ro', x, bY,'bo', x, gY, 'go')
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

