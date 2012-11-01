#! /usr/bin/env python

from technique import Technique
import cv

class RGBAnalysis( Technique ):
	def Analyse(self, image):
		'''Performs analysis using basic statistical techniques.

		Currently this returns a turple of the mean and the standard deviation: you can get hold of both by calling:

		(mean, stdDev) = Analyse(image).'''
		return cv.AvgSdv(image)

class HSVAnalysis( Technique ):
	def Analyse( self, image ):
		hsvImage = cv.CloneMat(image)
		cv.CvtColor( image, hsvImage, cv.CV_RGB2HSV )
		return cv.AvgSdv( hsvImage )

if __name__ == '__main__':
	raise ImportWarning('Intended as a library, not as a main class.')

