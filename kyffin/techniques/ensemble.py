from kyffin.techniques import Technique

class Ensemble(Technique):
    def __init__(self, *kargs):
        self.techniques = kargs

    def analyse(self, painting):
        return [technique.analyse(painting) for technique in self.techniques]
        

    def distance(self, current, other):
        distance = 0
        for i in range(len(self.techniques)):
            distance = distance + self.techniques[i].distance(current[i], other[i])
        return distance

    def export(self, data):
        return [technique.export(data) for technique in self.techniques]
