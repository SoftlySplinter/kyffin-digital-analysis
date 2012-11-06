from knn import KNearestNeighbour

def getML( name, technique ):
	if name == 'knn':
		return KNearestNeighbour( technique, 3 )
	else:
		return KNearestNeighbour( technique )
