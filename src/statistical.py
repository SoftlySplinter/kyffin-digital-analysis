#! /usr/bin/env python

from analysis import Analysis
import cv

class StatisticalAnalysis( Analysis ):
	def Analyse(self, image):
		'''Performs analysis using basic statistical techniques.

		Currently this returns a turple of the mean and the standard deviation: you can get hold of both by calling:

		(mean, stdDev) = Analyse(image).'''
		return cv.AvgSdv(image)

if __name__ == '__main__':
	raise ImportWarning('Intended as a library, not as a main class.')

