#! /usr/bin/env python

from optparse import OptionParser
import cv
import logging
import csv

DATA_DIR = 'data/'
LOG = logging.getLogger()
HANDLER = logging.StreamHandler()
HANDLER.setFormatter(logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s (%(filename)s:%(lineno)s)'))


def main():
	'''Quick down and dirty main method.'''
	parser = OptionParser()
	parser.add_option("-d", "--csv", dest="csv", help="Statistically analyse CSV file", metavar="CSV")
	parser.add_option("-l", "--loglevel", dest="loglevel", help="Set log level", default=logging.WARNING)

	(options, args) = parser.parse_args()
	
	LOG.setLevel(options.loglevel)
	HANDLER.setLevel(options.loglevel)
	LOG.addHandler(HANDLER)

	LOG.debug('Contents of parsed options: {0}'.format(options))
	
	if options.csv == None:
		LOG.error('No Input Data specified')
		raise ValueError('No Input Data specified')

	analyse(options.csv)

def analyse(data):
	'''Analyse a CSV file which contains the data for a set of images'''
	averages = dict()
	with open (data, 'r') as csvFile:
		dataReader = csv.reader(csvFile, delimiter=',', quotechar='"')
		for row in dataReader:
			avg = analyseRow(row)
			if avg is None:
				continue
			if row[1] not in averages:
				averages[row[1]] = [avg]
			else:
				averages[row[1]].append(avg)
	for (k,v) in averages.items():
		print '{0}: {1}'.format(k, v)

def analyseRow(row):
	'''Analyse a row in the CSV file.
	The format of these fils is as follows:

	0) Title
	1) Year
	2) Type
	3) Collection
	4) File'''
	try:
		image = cv.LoadImageM(DATA_DIR + row[4])
		return AverageRGB(image)
	except IOError:
		return None

def AverageRGB(image):
	'''Gets the average RGB values.
	Will return an CvScalar as this just wraps the OpenCV Avg function.'''
	return cv.Avg(image)

def StandardDeviationRGB(image):
	'''Gets the standard deviation of RGB values.
	Returns a CvScalar.
	Wraps the OpenCV AvgSdv'''
	(mean, stdDev) = cv.AvgSdv(image)
	return stdDev



if __name__ == '__main__':
	main()
#	raise ImportWarning('Intended as a library, not as a main class.')

