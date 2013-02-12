#! /usr/bin/env python

from kyffin.techniques import Technique
import cv
from datetime import date

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

    def get_attributes(self):
        return [('Year',          'NUMERIC'),
                ('Average Red',   'REAL'),
                ('Average Green', 'REAL'),
                ('Average Blue',  'REAL'),
                ('StdDev Red',    'REAL'),
                ('StdDev Green',  'REAL'),
                ('StdDev Blue',   'REAL')]

    def get_values(self, paintings):
        return [[int(painting.year), 
                 painting.data[0][0], 
                 painting.data[0][1],
                 painting.data[0][2],
                 painting.data[1][0],
                 painting.data[1][1],
                 painting.data[1][2]]
                for painting in paintings]


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
    def get_attributes(self):
        return [('Year',               'NUMERIC'),
                ('Average Hue',        'REAL'),
                ('Average Saturation', 'REAL'),
                ('Average Value',      'REAL'),
                ('StdDev Hue',         'REAL'),
                ('StdDev Saturation',  'REAL'),
                ('StdDev Value',       'REAL')]

    def get_values(self, paintings):
        return [[int(painting.year), 
                 painting.data[0][0], 
                 painting.data[0][1],
                 painting.data[0][2],
                 painting.data[1][0],
                 painting.data[1][1],
                 painting.data[1][2]]
                for painting in paintings]


if __name__ == '__main__':
    raise ImportWarning('Intended as a library, not as a main class.')

