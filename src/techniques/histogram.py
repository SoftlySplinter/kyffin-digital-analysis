#! /usr/bin/env python
import sys
import cv
from technique import Technique

class HistogramAnalysis(Technique):
        def __init__(self, bins = [255,255,255]):
		self.bins = bins

	def Analyse(self, image):
                r_range = [0,255]
                g_range = [0,255]
                b_range = [0,255]
                ranges = [r_range, g_range, b_range]

                # Set up the planes for RGB.
                r_plane = cv.CreateMat(image.rows, image.cols, cv.CV_8UC1)
                g_plane = cv.CreateMat(image.rows, image.cols, cv.CV_8UC1)
                b_plane = cv.CreateMat(image.rows, image.cols, cv.CV_8UC1)
                
                # Split the original image based on these planes and combine into an array for convenience.
                cv.Split(image, r_plane, g_plane, b_plane, None)
                planes = [r_plane, g_plane, b_plane]

		# Generate histograms with uniform bins.
		hist = cv.CreateHist(self.bins, cv.CV_HIST_ARRAY, ranges, 1)
		cv.CalcHist([cv.GetImage(i) for i in planes], hist)
		return hist

