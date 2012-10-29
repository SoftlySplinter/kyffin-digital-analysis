#! /usr/bin/env python

import cv
import csv

DATA_DIR = 'data/'

class Analyser:
	def __init__(self, technique, gui):
		self.technique = technique
		self.gui = gui

	def run(self, data):
		self.gui.render(self.analyse(data))

	def analyse(self, data):
		'''Analyse a CSV file which contains the data for a set of images'''
		analysedData = {}
		with open (data, 'r') as csvFile:
			dataReader = csv.reader(csvFile, delimiter=',', quotechar='"')
			for row in dataReader:
				avg = self.analyseRow(row)
				if avg is None:
					continue
				if row[1] not in analysedData:
					analysedData[row[1]] = [avg]
				else:
					analysedData[row[1]].append(avg)
				break
		return analysedData
		

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

