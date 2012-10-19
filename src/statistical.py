#! /usr/bin/env python

from optparse import OptionParser
import cv
import logging

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

LOG = logging.getLogger()
HANDLER = logging.StreamHandler()
HANDLER.setFormatter(logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s (%(filename)s:%(lineno)s)'))

def main():
	'''Quick down and dirty main method.'''
	parser = OptionParser()
	parser.add_option("-i", "--infile", dest="infile", help="Statistically analyse INFILE", metavar="INFILE")
	parser.add_option("-d", "--debug", dest="debug", action="store_true", help="Turn on debugging", default=False)

	(options, args) = parser.parse_args()
	
	if options.debug:
		LOG.setLevel(logging.DEBUG)
		HANDLER.setLevel(logging.DEBUG)
	else:
		HANDLER.setLevel(logging.WARNING)

	LOG.addHandler(HANDLER)

	LOG.debug('Contents of parsed options: {0}'.format(options))
	
	if options.infile == None:
		LOG.error('No Input File specified')
		raise ValueError('No Input File specified')

	image = cv.LoadImageM(options.infile)
	LOG.debug('Average: {0}'.format(AverageRGB(image)))
	LOG.debug('Std Dev: {0}'.format(StandardDeviationRGB(image)))

if __name__ == '__main__':
	main()
#	raise ImportWarning('Intended as a library, not as a main class.')

