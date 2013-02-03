#! /usr/bin/env python

from kyffin.techniques import Technique
import cv

class RGBAnalysis( Technique ):
    def analyse( self, painting ):
        try:
            image = cv.LoadImageM(painting.filePath)
            cv.AvgSdv(image)
            return cv.AvgSdv( image )
        except IOError as e:
            print 'Unable to load painting "{0}". {1}'.format(painting.title, e)

    def distance( self, a, b ):
        if b is None:
            return float('inf')

        distance = 0
        for i in range(len(a)):
            for j in range(len(a[i])):
                distance += abs(a[i][j] - b[i][j])
        return distance

class HSVAnalysis( Technique ):
    def analyse( self, painting ):
        try:
            image = cv.LoadImageM(painting.filePath)
            hsvImage = cv.CloneMat(image)
            cv.CvtColor( image, hsvImage, cv.CV_RGB2HSV )
            return cv.AvgSdv( hsvImage )
        except IOError as e:
            print 'Unable to load painting "{0}". {1}'.format(painting.title, e)
    def distance( self, a, b ):
        if b is None:
            return float('inf')

        distance = 0
        for i in range(len(a)):
            for j in range(len(a[i])):
                distance += abs(a[i][j] - b[i][j])
        return distance

if __name__ == '__main__':
    raise ImportWarning('Intended as a library, not as a main class.')

