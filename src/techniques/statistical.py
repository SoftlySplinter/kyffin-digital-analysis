#! /usr/bin/env python

from technique import Technique
import cv

class RGBAnalysis( Technique ):
	def Analyse( self, painting ):
		try:
			image = cv.LoadImageM(painting.filePath)
			cv.AvgSdv(image)
			painting.data = cv.AvgSdv( image )
		except IOError as e:
			print 'Unable to load painting "{0}". {1}'.format(painting.title, e)

class HSVAnalysis( Technique ):
	def Analyse( self, painting ):
		try:
			image = cv.LoadImageM(painting.filePath)
			hsvImage = cv.CloneMat(image)
			cv.CvtColor( image, hsvImage, cv.CV_RGB2HSV )
			painting.data = cv.AvgSdv( hsvImage )
		except IOError as e:
			print 'Unable to load painting "{0}". {1}'.format(painting.title, e)

if __name__ == '__main__':
	raise ImportWarning('Intended as a library, not as a main class.')

