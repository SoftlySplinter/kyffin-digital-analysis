import re
import logging

class KNearestNeighbourModal:
    def __init__( self, technique, k=1 ):
        self.technique = technique
        self.k = k

    def classify( self, meta, experience ):
        '''Classify the point in space.
        
        meta - The painting to classify.

        experience - A list of Painting objects.'''

        # Current closest is infinity to ease calculation
        kNearest = [float("inf")] * self.k
        years = [None] * self.k

        meta.year = None

        # Iterate through all experience and work out the distance
        for expMeta in experience:
#            if re.match('^\d\d\d\d$', expMeta.year) is None:
#                continue
            curDist = self.technique.distance(meta.data, expMeta.data)
            curYear = expMeta.year
            for i in range(self.k):
                if curDist < kNearest[i]:
                    # Swap kNearest[i] and curDist
                    temp = kNearest[i]
                    kNearest[i] = curDist
                    curDist = temp

                    # Do the swap for the year too
                    temp = years[i]
                    years[i] = curYear
                    curYear = temp

        years.sort()
        modal_year = int(years[len(years)/2])
        if len(years) % 2 == 0:
            modal_year = modal_year + int(years[(len(years)/2) - 1]) / 2
        meta.year = modal_year
