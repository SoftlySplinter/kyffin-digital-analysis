from math import cos, sin, exp, pi, ceil

import numpy
import cv2
import sys

def gabor(sigma,theta,g_lambda,psi,gamma):
    sigma_x = sigma;
    sigma_y = sigma/gamma;
 
    # Bounding box
    nstds = 3;
    xmax = max(abs(nstds*sigma_x*cos(theta)),abs(nstds*sigma_y*sin(theta)));
    xmax = ceil(max(1,xmax));
    ymax = max(abs(nstds*sigma_x*sin(theta)),abs(nstds*sigma_y*cos(theta)));
    ymax = ceil(max(1,ymax));
    xmin = -xmax; ymin = -ymax;
    [x,y] = numpy.meshgrid(xrange(int(xmin),int(xmax)),xrange(int(ymin),int(ymax)));
 
    # Rotation 
    x_theta=x*cos(theta)+y*sin(theta);
    y_theta=-x*sin(theta)+y*cos(theta);
 
    return exp(-.5*(float(x_theta)^2/sigma_x^2+float(y_theta)^2/sigma_y^2))*cos(2*pi/g_lambda*x_theta+psi);

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


        dim_y = xrange(int(min_x), int(max_x))
        dim_x = xrange(int(min_y), int(max_y))

        mat_x, mat_y = numpy.meshgrid(dim_y, dim_x)

        result = numpy.zeros(shape=(len(dim_x), len(dim_y)))

        for i in range(len(dim_x)):
            for j in range(len(dim_y)):
                result[i, j] = cls.gabor(mat_x[i, j], mat_y[i, j], 
                    sigma_x, sigma_y, 
                    theta, gab_lambda, psi)
            

        return result

    @classmethod
    def get_filters(cls, sigma = 0.5, gab_lambda = 1.0, psi = 0.0, gamma = 0.5):
        """ Gets the 4 standard filters.
        
        The default value chosen seem to produce the best correlation with 2nn 
        on Kyffin's paintings."""
        thetas = [0, pi/4, pi/2, (pi*3)/4]
        filters = dict()
        for theta in thetas:
            filters[theta] = cls.get_filter(sigma, theta, gab_lambda, psi, gamma)

        return filters

filter = GaborFilter()

image = cv2.imread(sys.argv[1], cv2.cv.CV_LOAD_IMAGE_GRAYSCALE)

cv2.imshow("",image)
cv2.waitKey()

for i in xrange(0,90, 5):
    
    theta = float(i)*(pi/180)
    print i
    dst = cv2.filter2D(image, -1, filter.get_filter(1.65,theta,0.5,2.,1.75))
    cv2.imshow("filtered ", dst)
    cv2.waitKey()
