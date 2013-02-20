from knn import KNearestNeighbour
from knn_modal import KNearestNeighbourModal
import re

def getML( name, technique ):
    knnRegex = re.compile('^\d+nn$')
    knn_modal_regex = re.compile('^\d+nn-modal$')
    if knnRegex.match(name):
        print 'Returning KNN Mean'
        m = knnRegex.search(name)
        k = m.group(0).replace('nn','')
        # Default k = 1
        if k is None:
            k = 1
        try:
            k = int(k)
        except ValueError:
            k = 1
        return KNearestNeighbour( technique, k )
    if knn_modal_regex.match(name):
        print 'Returning KNN Modal'
        m = knn_modal_regex.search(name)
        k = m.group(0).replace('nn-modal','')
        # Default k = 1
        if k is None:
            k = 1
        try:
            k = int(k)
        except ValueError:
            k = 1
        return KNearestNeighbourModal( technique, k )
        
    else:
        return KNearestNeighbour( technique )
