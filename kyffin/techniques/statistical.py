#! /usr/bin/env python

from kyffin.techniques import Technique
import cv2, numpy
from datetime import date, datetime

class RGBAnalysis( Technique ):
    def analyse( self, painting ):
        try:
            image = cv2.imread(painting.filePath)
            mean,std_dev = cv2.meanStdDev(image)
            return numpy.hstack((numpy.float32(mean), numpy.float32(std_dev)))
        except IOError as e:
            print 'Unable to load painting "{0}". {1}'.format(painting.title, e)

    def get_attributes(self):
        return [('Year',          'DATE %Y'),
                ('Average Red',   'REAL'),
                ('Average Green', 'REAL'),
                ('Average Blue',  'REAL'),
                ('StdDev Red',    'REAL'),
                ('StdDev Green',  'REAL'),
                ('StdDev Blue',   'REAL')]

    def get_values(self, paintings):
        return [[datetime.strptime(painting.year, '%Y'), 
                 painting.data[0][0], 
                 painting.data[0][1],
                 painting.data[0][2],
                 painting.data[1][0],
                 painting.data[1][1],
                 painting.data[1][2]]
                for painting in paintings]

#    def centroid(self, data):
#        count = [[0,0,0,0],[0,0,0,0]]
#        for painting in data:
#            for i in xrange(len(count)):
#                for j in xrange(len(count[i])):
#                    count[i][j] += painting.data[i][j]
#        for i in xrange(len(count)):
#            for j in xrange(len(count[i])):
#                count[i][j] /= len(data)
#        return count



class HSVAnalysis( Technique ):
    def analyse( self, painting ):
        try:
            image = cv2.imread(painting.filePath)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
            mean,std_dev = cv2.meanStdDev(image)
            return numpy.hstack((numpy.float32(mean), numpy.float32(std_dev)))
        except IOError as e:
            print 'Unable to load painting "{0}". {1}'.format(painting.title, e)
        except IOError as e:
            print 'Unable to load painting "{0}". {1}'.format(painting.title, e)

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

