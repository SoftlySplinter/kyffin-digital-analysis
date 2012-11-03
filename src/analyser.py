#! /usr/bin/env python

import csv
import painting as paint
import random, re

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

		randIndex = random.randint(0, len(self.paintings)-1)
		toClassify = self.paintings.pop(randIndex)

		self.gui.render(self.paintings)

		if re.match('^\d\d\d\d$', toClassify.year) is not None:
			print 'Known year of {0} is {1}'.format(toClassify.title, toClassify.year)
		elif re.match('^\d\d\d\d-\d\d\d\d$', toClassify.year) is not None:
			print 'Known year range of {0} is {1}'.format(toClassify.title, toClassify.year)
		else:
			print 'Year of {0} is unknown'.format(toClassify.title)

		self.ml.classify( toClassify, self.paintings )

		print 'Classified date is: {0}'.format(toClassify.year)

	def analyse(self):
		for painting in self.paintings:
			self.technique.Analyse(painting)
		

	def loadPaintings( self, data ):
		with open( data, 'r' ) as csvFile:
			dataReader = csv.reader(csvFile, delimiter=',', quotechar='"')
			for row in dataReader:
				try:
					self.paintings.append(paint.load(row, DATA_DIR))
				except IOError:
					continue
				

if __name__ == '__main__':
	raise ImportWarning('Intended as a library, not as a main class.')

