'''
Contains useful techniques for performing Edge Orientation.
'''

from src.techniques.technique import Technique
import cv

class EdgeOrientation(Technique):
    '''Perform the edge orientation technique.'''
 
    DEFAULT = 'canny'
    def __init__(self, algorithm = DEFAULT):
        self.algorithm = algorithm

    def analyse(self, painting):
        '''Analyse the given painting.'''
        painting.data = self.edge(painting)

    def edge(self, painting):
        '''Perform edge detection. The algorithm used is defined by 
        `self.algormth`.'''
        if self.algorithm == 'sobel':
            return self.sobel_edge(painting)
        elif self.algorithm == 'canny':
            return self.canny_edge(painting)
        elif self.algorithm == 'scharr':
            return self.scharr_edge(painting)
        # Default to canny in a hard-coded way.
        else:
            return self.canny_edge(painting)

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
        print current
        print other
        return 0
