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
		kNearest = [float("inf")] * self.k
		years = [None] * self.k

		meta.year = None

		if meta.data is None:
			logging.info('Painting {0} was not analysed.'.format(meta.title))
			return

		# Iterate through all experience and work out the distance
		for expMeta in experience:
			if re.match('^\d\d\d\d$', expMeta.year) is None:
				continue
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

		logging.debug('KNearest: ' + ', '.join(years))

		meanYear = 0
		for year in years:
			meanYear += int(year)
		meanYear /= len(years)
		meta.year = meanYear
