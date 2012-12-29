from math import cos, sin, exp, pi, ceil

import numpy

class GaborFilter:
    def __init__(self):
        pass

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
    def get_filter(cls, sigma, theta, gab_lambda, psi, gamma):
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


        dim_y = len(range(int(min_x), int(max_x)))
        dim_x = len(range(int(min_y), int(max_y)))

        mat_x, mat_y = numpy.meshgrid(dim_y, dim_x)

        result = numpy.zeros(shape=(dim_x, dim_y))

        for i in range(dim_x):
            for j in range(dim_y):
                result[i, j] = cls.gabor(mat_x[i, j], mat_y[i, j], 
                    sigma_x, sigma_y, 
                    theta, gab_lambda, psi)
            

        return result

    @classmethod
    def get_filters(cls, sigma = 1.0, gab_lambda = 1.0, psi = 0.0, gamma = 1.0):
        thetas = [0, pi/4, pi/2, (pi*3)/4]
        filters = dict()
        for theta in thetas:
            filters[theta] = cls.get_filter(sigma, theta, gab_lambda, psi, gamma)

        return filters
