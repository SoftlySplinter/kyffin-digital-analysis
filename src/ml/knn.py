

class KNearestNeighbour:
	def classify( meta, experience, distanceMeasure ):
		'''Classify the point in space.
		
		meta - The painting to classify.

		experience - A list of Painting objects.'''

		# Current closest is infinity to ease calculation
		closestDistance = float("inf")
		year = None

		# Iterate through all experience and work out the distance
		for expMeta in experience:
			curDist = distanceMeasure.difference(meta.location, expMeta)
			if curDist < closestDistance:
				closestDistance = curDist
				year = expMeta.year

		meta.year = year
