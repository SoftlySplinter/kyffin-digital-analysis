'''
Contains useful techniques for performing Edge Orientation.
'''

__all__ = ['EdgeOrientation']

from kyffin.techniques import Technique
from kyffin.techniques.steerable_filter import SteerableFilter
from kyffin.techniques.gabor_filter import GaborFilter
import cv2, numpy

class EdgeOrientation(Technique):
    '''Perform the edge orientation technique.'''
    def analyse(self, painting):
        image = cv2.imread(painting.filePath, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        image = cv2.Canny(image, 100., 200.)
        return cv2.calcHist(image, [0], None, [2], [0,1])
