__all__ = ['Technique']

from abc import abstractmethod
import arff
import datetime
import cv2

class Technique( object ):
    '''Abstract class to define a technique.'''

    def analyse(self, painting):
        '''Perform some form of analysis on a painting.'''
        return None

    def distance(self, current, other):
        '''Return a distance metric from one analysed painting to another.'''
        return cv2.compareHist(current, other, cv2.cv.CV_COMP_CHISQR)

    def centroid(self, paintings):
        return numpy.mean([painting.data for painting in paintings], axis=0)

    def export(self, paintings):
        """Export the analysed data."""
        data = {'description': self.__class__.__name__, 
                'relation': 'year', 
                'attributes': self.get_attributes(), 
                'data': self.get_values(paintings)}
        return arff.dumps(data)

    def get_values(self, paintings):
        return [[datetime.date(int(painting.year),1, 1)] for painting in paintings]

    def get_attributes(self):
        return [('year', 'DATE')]
