import re

class KNearestNeighbour:
	def __init__( self, technique ):
		self.technique = technique

	def classify( self, meta, experience ):
		'''Classify the point in space.
		
		meta - The painting to classify.

		experience - A list of Painting objects.'''

		# Current closest is infinity to ease calculation
		closestDistance = float("inf")
		year = None

		meta.year = 'Unclassified.'

		if meta.data is None:
			print 'Painting {0} was not analysed.'.format(meta.title)
			return

		# Iterate through all experience and work out the distance
		for expMeta in experience:
			if re.match('^\d\d\d\d$', expMeta.year) is None:
				continue
			curDist = self.technique.distance(meta.data, expMeta.data)
			if curDist < closestDistance:
				closestDistance = curDist
				year = expMeta.year

		meta.year = year
