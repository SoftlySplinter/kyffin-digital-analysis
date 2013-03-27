from math import cos, sin, exp, pi, ceil

import numpy
import cv2
from kyffin.techniques import Technique

class GaborFilter(Technique):
    def __init__(self, orientations):
        self.orientations = orientations

    def analyse(self, painting):
        image = cv2.imread(painting.filePath, cv2.cv.CV_LOAD_IMAGE_GRAYSCALE)
        data = [cv2.filter2D(image, cv2.cv.CV_32F, self.get_filter(orientation)) for orientation in self.orientations]
        return numpy.array([cv2.calcHist([d], [0], None, [2], [0,255]) for d in data])

    @classmethod
    def gabor(cls, cur_x, cur_y, 
            sigma_x, sigma_y, 
            theta, gab_lambda, psi):
        theta_x = cur_x * cos(theta) + cur_y * sin(theta)
        theta_y = -(cur_x * sin(theta)) + cur_y * cos(theta)

        return exp(
            -0.5 * 
           (pow(theta_x, 2) / pow(sigma_x, 2) + 
           pow(theta_y, 2) / pow(sigma_y, 2))
        ) * cos(
            2 * pi / gab_lambda * theta_x+psi)

    @classmethod
    # From wikipedia's MATLAB code.
    def get_filter(cls, sigma, theta=0.5, gab_lambda=1., psi=0., gamma=0.5):
        sigma_x = sigma
        sigma_y = sigma/gamma

        # Bounding box
        nstds = 3
        max_x = max(
            abs(nstds * sigma_x * cos(theta)), 
            abs(nstds * sigma_y * sin(theta)))
        max_x = ceil(max(1, max_x))

        max_y = max(
            abs(nstds * sigma_x * sin(theta)), 
            abs(nstds * sigma_y * cos(theta)))
        max_y = ceil(max(1, max_y))

        min_x = -max_x
        min_y = -max_y


        dim_y = range(int(min_x), int(max_x))
        dim_x = range(int(min_y), int(max_y))

        mat_x, mat_y = numpy.meshgrid(dim_y, dim_x)

        result = numpy.zeros((len(dim_x), len(dim_y)), numpy.float32)

        for i in range(len(dim_x)):
            for j in range(len(dim_y)):
                result[i, j] = cls.gabor(mat_x[i, j], mat_y[i, j], 
                    sigma_x, sigma_y, 
                    theta, gab_lambda, psi)
            

        return result

    @classmethod
    def get_filters(cls, sigma = 1.0, gab_lambda = 1.0, psi = 0.0, gamma = 0.5):
        """ Gets the 4 standard filters.
        
        The default value chosen seem to produce the best correlation with 2nn 
        on Kyffin's paintings."""
        thetas = [0, pi/4, pi/2, (pi*3)/4]
        filters = dict()
        for theta in thetas:
            filters[theta] = cls.get_filter(sigma, theta, gab_lambda, psi, gamma)

        return filters
