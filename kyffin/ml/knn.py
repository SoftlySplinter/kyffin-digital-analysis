import re
import logging
import scipy.stats as stats
import matplotlib.pyplot as plot

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

        return self.average(years)

    def visualise(self, actual, classified):
        (correlation, unknown) = self.correlation(classified, actual)
        print '{0}\t{1}'.format(correlation, unknown)

        plot.figure(2)
        plot.plot(actual, classified, 'x')
        plot.xlabel('Actual Year')
        plot.ylabel('Classified Year')
#        plot.show()

    def correlation(self, classified, actual):
        a = [float(x) for x in classified]
        b = [float(x) for x in actual]
        return stats.pearsonr(a, b)

    def average(self, years):
        meanYear = 0
        for year in years:
            meanYear += int(year)
        meanYear /= len(years)
        return meanYear

class KNearestNeighbourModal(KNearestNeighbour):
    def average(self, years):
        years.sort()
        modal_year = int(years[len(years)/2])
        if len(years) % 2 == 0:
            modal_year = modal_year + int(years[(len(years)/2) - 1]) / 2
        return modal_year
