""" Adds histogram of edges to a colour histogram of the painting. """

import cv
from kyffin.techniques.technique import Technique
from kyffin.techniques.histogram import HistogramAnalysis
from kyffin.techniques.edge_orientation import EdgeOrientation

class ColourEdgeHistogramAnalysis(Technique):
    def analyse(self, painting):
        pass

    def distance(self, current, other):
        return 0
