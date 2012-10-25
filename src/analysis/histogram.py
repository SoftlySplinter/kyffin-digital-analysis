#! /usr/bin/env python
import cv
from analysis import Analysis

class HistogramAnalysis(Analysis):
	def __init__(self, dims=[255,255,255], ranges=[[0,255],[0,255],[254,255]]):
		self.dims = dims
		self.ranges = ranges

	def Analyse(self, image):
		histogram = cv.CreateHist(self.dims, cv.CV_HIST_ARRAY, self.ranges)
		cv.CreateHist([image], histogram)
		return histogram
