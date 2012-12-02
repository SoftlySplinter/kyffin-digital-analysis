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
    def get_filter(cls, orientation, kernel_size = 3, transpose = False, strength = -1):
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

        matrix = numpy.ones((kernel_size, kernel_size), numpy.float32)

        for i in range(kernel_size):
            if orientation == 0:
                matrix[i, kernel_size/2] = strength
            if orientation == pi/4:
                matrix[i, kernel_size - i - 1] = strength
            if orientation == pi/2:
                matrix[kernel_size/2, i] = strength
            if orientation == (3*pi)/4:
                matrix[i, i] = strength

        if transpose:
            for i in range(kernel_size):
                for j in range(kernel_size):
                    if matrix[i, j] == strength:
                        matrix[i, j] = 1
                    else:
                        matrix[i, j] = strength

        return matrix
    

    @classmethod
    def valid_orientation(cls, orientation):
        '''Check the orientation of the filter is valid'''
        # 45 degrees (pi/4) is valid.
        return orientation % (pi/4) == 0

def main():
    '''Testing Main method'''
    import sys, cv

    if len(sys.argv) == 1:
        print 'No image.'
        sys.exit(1)

    im_file = sys.argv[1]
    image = cv.LoadImageM(im_file, cv.CV_LOAD_IMAGE_GRAYSCALE)

    size = 3
    ori = pi/4
    ste = -1.

    kern = cv.fromarray(SteerableFilter.get_filter(ori, size, False, ste))
    kern_t = cv.fromarray(SteerableFilter.get_filter(ori, size, True, ste))

    kernel = cv.CreateMat(size, size, cv.CV_32F)
    kernel_t = cv.CreateMat(size, size, cv.CV_32F)

    cv.Convert(kern, kernel)
    cv.Convert(kern_t, kernel_t)


    dst = cv.CreateMat(image.rows, image.cols, image.type)
    dst_t = cv.CreateMat(image.rows, image.cols, image.type)
    cv.Filter2D(image, dst, kernel)
    cv.Filter2D(image, dst_t, kernel_t)

    cv.ShowImage('Source', image)
    cv.ShowImage('Result', dst)
    cv.ShowImage('Result (Transpose)', dst_t)
    cv.WaitKey(0)

if __name__ == '__main__':
    main()
