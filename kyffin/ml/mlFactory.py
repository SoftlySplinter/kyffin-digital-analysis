from kyffin.ml.knn import KNearestNeighbour
from kyffin.ml.knn import KNearestNeighbourModal
from kyffin.ml.nearest_exemplar import NearestExemplar
from kyffin.ml.statistical_exemplar import TheoreticalStatisticalExemplar, RealStatisticalExemplar
import re

def getML( name, technique ):
    knnRegex = re.compile('^\d+nn$')
    knn_modal_regex = re.compile('^\d+nn-modal$')
    if knnRegex.match(name):
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
    if "statistical-exemplar" in name:
        return RealStatisticalExemplar(technique, "./exemplar.csv")
    if "theoretical-exemplar" in name:
        return TheoreticalStatisticalExemplar(technique, "./exemplar.csv")
    else:
        raise Exception("Technique '{}' unknown".format(name))
