from knn import KNearestNeighbour
import re

def getML( name, technique ):
	knnRegex = re.compile('(.)nn')
	if knnRegex.match(name):
		m = knnRegex.search(name)
		k = m.group(0)

		# Default k = 1
		if k is None:
			k = 1

		# Cast to int
		try:
			k = int(k)
		except ValueError:
			k = 1

		return KNearestNeighbour( technique, k )
	else:
		return KNearestNeighbour( technique )
