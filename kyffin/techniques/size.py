from kyffin.techniques import Technique
import numpy

class Size(Technique):
    def analyse(self, painting):
        return numpy.array([painting.height, painting.width], dtype=numpy.float32)
