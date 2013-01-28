'''
Contains useful techniques for performing Edge Orientation.
'''

from kyffin.techniques.technique import Technique
from kyffin.techniques.steerable_filter import SteerableFilter
from kyffin.techniques.gabor_filter import GaborFilter
import cv, numpy

class EdgeOrientation(Technique):
    '''Perform the edge orientation technique.'''
 
    DEFAULT_ALGORITHM = 'gabor'
    DEFAULT_EDGE = None
    def __init__(self, edge = DEFAULT_EDGE, algorithm = DEFAULT_ALGORITHM):
        self.edge = edge
        self.algorithm = algorithm

    def analyse(self, painting):
        edge = self.edge_detection(painting)
        painting.data = self.orientation(edge)

    def orientation(self, image):
        '''Get the orientation of edges in a painting.'''
        filters = None
        intensities = dict()

        if self.algorithm == 'steerable':
            filters = SteerableFilter.get_filters(3, False, 0)
        elif self.algorithm == 'gabor':
            filters = GaborFilter.get_filters()

        for key in filters:
            intensities[key] = self.apply_filter(filters[key], image)
        return intensities

    def apply_filter(self, filt, image):
        """Apply a filter to an image."""
        kern = cv.fromarray(filt)
        kernel = cv.CreateMat(kern.rows, kern.cols, cv.CV_32F)
        cv.Convert(kern, kernel)
        dst = cv.CreateMat(image.rows, image.cols, image.type)
        cv.Filter2D(image, dst, kernel)

        return dst

    def edge_detection(self, painting):
        '''Perform edge detection. The algorithm used is defined by 
        `self.algormth`.'''
        if self.edge == 'sobel':
            return self.sobel_edge(painting)
        elif self.edge == 'canny':
            return self.canny_edge(painting)
        elif self.edge == 'scharr':
            return self.scharr_edge(painting)
        # Default to canny in a hard-coded way.
        else:
            return cv.LoadImageM(painting.filePath, cv.CV_LOAD_IMAGE_GRAYSCALE)

    @classmethod
    def sobel_edge(cls, painting):
        '''Perform Sobel Edge Detection.'''

        # Load the image.
        src = cv.LoadImageM(painting.filePath, cv.CV_LOAD_IMAGE_GRAYSCALE)

        # Sobel needs a 16-bit Signed value to prevent overflow.
        dst = cv.CreateMat(src.height, src.width, cv.CV_16S)

        # Smooth before performing.
        cv.Smooth(src, src, cv.CV_BLUR, 3, 3)

        # Perform Sobel.
        cv.Sobel(src, dst, 1, 1, 5)

        # Convert back to a 8-bit unsigned value for convenience.
        ret = cv.CreateMat(src.height, src.width, cv.CV_8U)
        cv.ConvertScaleAbs(dst, ret)

        return ret

    @classmethod
    def canny_edge(cls, painting):
        '''Perform Canny Edge Detection.'''

        # Load the image.
        src = cv.LoadImageM(painting.filePath, cv.CV_LOAD_IMAGE_GRAYSCALE)

        # Canny needs the same type of destination.
        dst = cv.CreateMat(src.height, src.width, src.type)

        # Smooth before performing.
        cv.Smooth(src, src, cv.CV_BLUR, 3, 3)

        # Perform canny.
        cv.Canny(src, dst, 100.0, 200.0)

        return dst

    @classmethod
    def scharr_edge(cls, painting):
        '''Apply a Scharr Operator to the painting.
        
        To do this I've had to added the two different directions Scharr can work with (x 
        and y) using OpenCV's AddWeighted.'''

        # Load the image.
        src = cv.LoadImageM(painting.filePath, cv.CV_LOAD_IMAGE_GRAYSCALE)

        # Smooth before performing the edge detection.
        cv.Smooth(src, src, cv.CV_BLUR, 3, 3)

        # As Scharr uses Sobel in OpenCV, the destinations need to be 16-bit 
        # signed.
        dst_x = cv.CreateMat(src.height, src.width, cv.CV_16S)
        dst_y = cv.CreateMat(src.height, src.width, cv.CV_16S)

        # Perform Scharr in both axes.
        cv.Sobel(src, dst_x, 1, 0, cv.CV_SCHARR)
        cv.Sobel(src, dst_y, 0, 1, cv.CV_SCHARR)
        
        # Convert back to 8-bit unsigned
        ret_x = cv.CreateMat(src.height, src.width, cv.CV_8U)
        ret_y = cv.CreateMat(src.height, src.width, cv.CV_8U)

        cv.ConvertScaleAbs(dst_x, ret_x)
        cv.ConvertScaleAbs(dst_y, ret_y)

        # Add the two axes together equally.
        ret = cv.CreateMat(src.height, src.width, cv.CV_8U)
        cv.AddWeighted(ret_x, 0.5, ret_y, 0.5, 0, ret)

        return ret

    @classmethod
    def distance(cls, current, other):
        '''Returns a distance metric between one analysed painting and the 
        other.'''
        distance = 0
        for i in current.keys():
            distance = distance + cls.compare(current[i], other[i])
        return distance

    @classmethod
    def compare(cls, cur_data, other_data):
        """Compare two filters of the same orientation."""

        # TODO Work out if there's a better method for comparison.
        (cur, _, _, _) = cv.Avg(cur_data)
        (oth, _, _, _) = cv.Avg(other_data)

        return abs(cur - oth)
