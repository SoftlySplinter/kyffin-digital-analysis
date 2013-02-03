'''Overarching technique class.'''

from abc import abstractmethod

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
