#! /usr/bin/env python

import csv
import painting as paint
import random, re
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

		randIndex = random.randint(0, len(self.paintings)-1)
		toClassify = self.paintings.pop(randIndex)

		self.gui.render(self.paintings)

		knownYear = toClassify.year
		self.ml.classify( toClassify, self.paintings )

		if re.match('^\d\d\d\d$', knownYear) is not None:
			print 'Known year of {0} is {1}'.format(toClassify.title, knownYear)
			classifiedYear = int(toClassify.year)
			actualYear = int(knownYear)
			error = abs(actualYear - classifiedYear)
			print 'Classified date is: {0} (Error of {1})'.format(toClassify.year, error)
		elif re.match('^\d\d\d\d-\d\d\d\d$', knownYear) is not None:
			print 'Known year range of {0} is {1}'.format(toClassify.title, knownYear)
			yearRange = knownYear.split('-')
			fromYear = int(yearRange[0])
			toYear = int(yearRange[1])
			classifiedYear = int(toClassify.year)

			error = 0
			if classifiedYear > toYear:
				error = abs(toYear - classifiedYear)
			elif classifiedYear < fromYear:
				error = abs(fromYear - classifiedYear)

			print 'Classified date is: {0} (Error of {1})'.format(toClassify.year, error)
		else:
			print 'Year of {0} is unknown'.format(toClassify.title)
			print 'Classified date is: {0}'.format(toClassify.year)



	def analyse(self):
		for painting in self.paintings:
			self.technique.Analyse(painting)
		

	def loadPaintings( self, data ):
		with open( data, 'r' ) as csvFile:
			dataReader = csv.reader(csvFile, delimiter=',', quotechar='"')
			for row in dataReader:
				try:
					painting = paint.load(row, DATA_DIR)
					if os.path.isfile(painting.filePath):
						self.paintings.append(painting)
					else:
						logging.warning('Unable to load {0}: File {1} does not exist'.format(painting.title, painting.filePath))
				except IOError:
					continue
				

if __name__ == '__main__':
	raise ImportWarning('Intended as a library, not as a main class.')

