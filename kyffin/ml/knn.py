import re
import logging

class KNearestNeighbour:
    def __init__( self, technique, k=1 ):
        self.technique = technique
        self.k = k

    def classify( self, meta, experience ):
        '''Classify the point in space.
        
        meta - The painting to classify.

        experience - A list of Painting objects.'''
        # Current closest is infinity to ease calculation
        kNearest = [-1] * self.k
        years = [None] * self.k

        # Iterate through all experience and work out the distance
        for expMeta in experience:
            curDist = self.technique.distance(meta.data, expMeta.data)
            curYear = expMeta.year
            for i in xrange(self.k):
                if curDist < kNearest[i] or kNearest[i] == -1:
                    # Swap kNearest[i] and curDist
                    temp = kNearest[i]
                    kNearest[i] = curDist
                    curDist = temp

                    # Do the swap for the year too
                    temp = years[i]
                    years[i] = curYear
                    curYear = temp
        meanYear = 0
        for year in years:
            meanYear += int(year)
        meanYear /= len(years)

        return meanYear
