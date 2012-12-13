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

    -1  1 -1
    -1  1 -1
    -1  1 -1
    '''


    def __init__(self):
        pass

    @classmethod
    def get_filter(cls, orientation, kernel_size = 3, transpose = False, strength = 0):
        '''
        Gets the filter in the form of a numpy matrix, which can easily be 
        changed into an OpenCV material to be used with cv.Filter2D.

        The orientation can be one of: 0, pi/4, pi/2, 3 pi/4 radians 
        (0, 45, 90 or 135 degrees for non-mathematicians).

        The kernel size is fairly self-explanitory. The line will always be 
        central to the kernel.

        Transpose inverts the filter.

        Strength relates to the strength of the filter. A strength of X, where
        X != 0 relates to "positive" elements being -X, and any others being X.

        A strength of 0 relates to positive elements being 0 and any others 
        being 1
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

        # Create the matrix
        matrix = numpy.ones((kernel_size, kernel_size), numpy.float32)

        # For standard cases, make all the elements in the matrix equal to the
        # strength.
        if strength != 0:
            for i in range(kernel_size):
                for j in range(kernel_size):
                    matrix[i, j] *= strength

        # Add the positive examples
        for i in range(kernel_size):
            x = 0
            y = 0

            # 0   degree line
            if orientation == 0:
                x = i
                y = kernel_size/2
            # 45  degree line
            if orientation == pi/4:
                x = i
                y = kernel_size - i - 1
            # 90  degree line
            if orientation == pi/2:
                x = kernel_size/2
                y = i
            # 135 degree line
            if orientation == (3*pi)/4:
                x = i
                y = i

            # Normal cases invert the value.
            if strength != 0:
                matrix[x, y] *= -1
            # 0 case sets value to 0.
            else:
                matrix[x, y] = 0

        # Transpose if needed
        if transpose:
            for i in range(kernel_size):
                for j in range(kernel_size):
                        # Flip is transpose for 0 strength
                        if strength == 0:
                            val = int(matrix[i, j])
                            matrix[i, j] = val ^ 1
                        # Invert if not 0 strength
                        else:
                            matrix[i, j] *= -1

        return matrix
    

    @classmethod
    def valid_orientation(cls, orientation):
        '''Check the orientation of the filter is valid'''
        # 45 degrees (pi/4) is valid.
        return orientation % (pi/4) == 0

    @classmethod
    def get_filters(cls, kernel_size = 3, inverse = False, strength = 0):
        orientations = [0, pi/4, pi/2, (pi*3)/4]
        filters = dict()

        for orientation in orientations:
            filters[orientation] = cls.get_filter(orientation, kernel_size, inverse, strength)

        return filters

def main():
    '''Testing Main method'''
    import sys, cv

    if len(sys.argv) == 1:
        print 'No image.'
        sys.exit(1)

    im_file = sys.argv[1]
    image = cv.LoadImageM(im_file, cv.CV_LOAD_IMAGE_GRAYSCALE)

    size = 3
    ori = (pi*3)/4
    ste = 3

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
    cv.WaitKey(0)
    cv.WaitKey(0)

if __name__ == '__main__':
    main()
