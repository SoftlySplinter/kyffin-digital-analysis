""" Adds histogram of edges to a colour histogram of the painting. """

import cv
from kyffin.techniques.technique import Technique
from kyffin.techniques.histogram import HistogramAnalysis
from kyffin.techniques.edge_orientation import EdgeOrientation

class ColourEdgeHistogramAnalysis(Technique):
    def analyse(self, painting):
        hist_ana = HistogramAnalysis([5,5,5])
        hist_ana.analyse(painting)
        hist = painting.data

        edge_ana = EdgeOrientation()
        edge_ana.analyse(painting)
        # TODO add the edges to the colour histogram.

        # Set the painting data back to the histogram.
        painting.data = hist

    def distance(self, current, other):
        return 0
