'''
Module for the Steerable Filter class.
'''

from math import pi
import numpy

class SteerableFilter:
    '''
    Defines a steerable filter

    That is: a simple N x N matrix which can take orientations of 0, 45, 90 and
    135 degrees (0, pi/4, pi/2, 3pi/4 radians) and creates a filter which has a
    line of 1's down the centre with the gradient of that line being equal to 
    the orientation.

    e.g. For orientation=0, kernel size=3, the filter would be:

    0 1 0
    0 1 0
    0 1 0
    '''


    def __init__(self):
        pass

    @classmethod
    def get_filter(cls, orientation, kernel_size = 3):
        '''
        Gets the filter in the form of a numpy matrix, which can easily be 
        changed into an OpenCV material to be used with cv.Filter2D.
        '''
        if kernel_size % 2 == 0:
            raise RuntimeError(
                'Kernel size of \'{0}\' is not valid: must be odd'
                    .format(kernel_size))

        # Modulo orientation to ensure it's within 2pi
        orientation %= pi

        if not cls.valid_orientation(orientation):
            raise RuntimeError(
                 'Orientation \'{0}\' is not valid for kernel size \'{1}\''
                     .format(orientation, kernel_size))

        matrix = numpy.zeros((kernel_size, kernel_size))

        for i in range(kernel_size):
            if orientation == 0:
                matrix[i, kernel_size/2] = 1
            if orientation == pi/4:
                matrix[i, kernel_size - i - 1] = 1
            if orientation == pi/2:
                matrix[kernel_size/2, i] = 1
            if orientation == (3*pi)/4:
                matrix[i, i] = 1

        return matrix
    

    @classmethod
    def valid_orientation(cls, orientation):
        '''Check the orientation of the filter is valid'''
        # 45 degrees (pi/4) is valid.
        return orientation % (pi/4) == 0
