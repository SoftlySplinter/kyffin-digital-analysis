#! /usr/bin/env python
import sys
import cv
import cv2
from kyffin.techniques import Technique
from tempfile import NamedTemporaryFile
import yaml
from scipy.cluster.vq import kmeans2
import numpy

class HistogramAnalysis(Technique):
    def __init__(self, bins = 256):
        self.bins = bins

    def analyse(self, painting):
        image = cv2.imread(painting.filePath)
        image = self.convert(image)
        data = [cv2.calcHist([channel], [0], None, [self.bins], [0,255]) for channel in cv2.split(image)]
        return numpy.array(data)

    def convert(self, image):
        return image

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

class HSVHistogramAnalysis(HistogramAnalysis):
    def convert(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
