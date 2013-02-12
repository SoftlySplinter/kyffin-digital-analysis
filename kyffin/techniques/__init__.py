__all__ = ['Technique']

from abc import abstractmethod
import arff
import datetime

class Technique( object ):
    '''Abstract class to define a technique.'''

    @abstractmethod
    def analyse(self, painting):
        '''Perform some form of analysis on a painting.'''
        return None

    @abstractmethod
    def distance(self, current, other):
        '''Return a distance metric from one analysed painting to another.'''
        pass

    def export(self, paintings):
        """Export the analysed data."""
        data = {'description': self.__class__.__name__, 
                'relation': 'year', 
                'attributes': self.get_attributes(), 
                'data': self.get_data(paintings)}
        return arff.dumps(data)

    @abstractmethod
    def get_data(self, paintings):
        return [[datetime.date(int(painting.year),1, 1)] for painting in paintings]

    def get_attributes(self):
        return [('year', 'DATE')]
