#! /usr/bin/env python

import csv
import painting as paint

DATA_DIR = 'data/'

class Analyser:
	def __init__(self, technique, gui):
		self.technique = technique
		self.gui = gui
		self.paintings = []

	def run(self, data):
		self.loadPaintings( data )
		self.analyse()
		self.gui.render(self.paintings)

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

