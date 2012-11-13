#! /usr/bin/env python

import csv
import painting as paint
import random, re
import matplotlib.pyplot as plot
import os.path
import logging

DATA_DIR = 'data/'

class Analyser:
	def __init__(self, technique, gui, ml):
		self.technique = technique
		self.gui = gui
		self.ml = ml
		
		self.paintings = []

	def run(self, data):
		self.loadPaintings( data )
		self.analyse()

		actual = []
		classified = []

		for i in range(len(self.paintings)):
			toClassify = self.paintings.pop(i)
			actualY = toClassify.year

#			self.gui.render(self.paintings)

#		if re.match('^\d\d\d\d$', toClassify.year) is not None:
#			print 'Known year of {0} is {1}'.format(toClassify.title, toClassify.year)
#		elif re.match('^\d\d\d\d-\d\d\d\d$', toClassify.year) is not None:
#			print 'Known year range of {0} is {1}'.format(toClassify.title, toClassify.year)
#		else:
#			print 'Year of {0} is unknown'.format(toClassify.title)

			self.ml.classify( toClassify, self.paintings )

			classifiedY = toClassify.year

			toClassify.year = actualY
			self.paintings.insert(i, toClassify)

			actual.append(actualY)
			classified.append(classifiedY)


		plot.plot(actual, classified, 'x')
		plot.xlabel('Actual Year')
		plot.ylabel('Classified Year')
		plot.show()

#		print 'Classified date is: {0}'.format(toClassify.year)

	def analyse(self):
		for painting in self.paintings:
			self.technique.Analyse(painting)
		

	def loadPaintings( self, data ):
		with open( data, 'r' ) as csvFile:
			dataReader = csv.reader(csvFile, delimiter=',', quotechar='"')
			for row in dataReader:
				try:
					painting = paint.load(row, DATA_DIR)
					if re.match('^\d\d\d\d$', painting.year):
						self.paintings.append(painting)

					if os.path.isfile(painting.filePath):
						self.paintings.append(painting)
					else:
						logging.warning('Unable to load {0}: File {1} does not exist'.format(painting.title, painting.filePath))
				except IOError:
					continue
				

if __name__ == '__main__':
	raise ImportWarning('Intended as a library, not as a main class.')

