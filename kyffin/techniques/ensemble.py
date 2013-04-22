from kyffin.techniques import Technique
import numpy

class Ensemble(Technique):
    def __init__(self, *kargs):
        self.techniques = kargs

    def analyse(self, painting):
        arr = [technique.analyse(painting).flatten() for technique in self.techniques]
#        print arr
#        print numpy.concatenate(arr)
        return numpy.concatenate(arr)

    def export(self, data):
        return [technique.export(data) for technique in self.techniques]
