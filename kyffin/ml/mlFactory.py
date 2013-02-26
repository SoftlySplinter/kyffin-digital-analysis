from kyffin.ml.knn import KNearestNeighbour
from kyffin.ml.knn_modal import KNearestNeighbourModal
from kyffin.ml.nearest_exemplar import NearestExemplar
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
    if "nearest-exemplar" in name:
        return NearestExemplar(technique, "./exemplar.csv")
    else:
        return KNearestNeighbour( technique )
