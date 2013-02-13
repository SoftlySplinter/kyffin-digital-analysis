#! /usr/bin/env python
import sys
import cv
from kyffin.techniques import Technique
from tempfile import NamedTemporaryFile
import yaml

class HistogramAnalysis(Technique):
    def __init__(self, bins = [255,255,255]):
        self.bins = bins

    def analyse(self, painting):
        image = None
        try:
            image = cv.LoadImageM( painting.filePath )
        except IOError as e:
            print 'Unable to load {0}: {1}'.format(painting.title, e)
            return

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

    def distance(self, a, b):
        return cv.CompareHist(a,b,cv.CV_COMP_CHISQR)

    def get_values(self, paintings):
        return [[painting.year] + self.export_cv(painting) for painting in paintings] 

    def get_attributes(self):
        atts = []
        for i in xrange(self.bins[0]):
            for j in xrange(self.bins[1]):
                for k in xrange(self.bins[2]):
                    atts.append(('{}, {}, {}'.format(i, j, k), 'REAL'))
        return [('year', 'INTEGER')] + atts
                

    def export_cv(self, painting):
        data = []
        for i in xrange(self.bins[0]):
            for j in xrange(self.bins[1]):
                for k in xrange(self.bins[2]):
                    data.append(cv.QueryHistValue_3D(painting.data, i, j, k))
        return data
