"""Classified based on the nearest exemplar."""
import csv
from kyffin.ml.knn import KNearestNeighbour
from kyffin.ml.nearest_exemplar import NearestExemplar, FakePainting
import sys

class TheoreticalStatisticalExemplar(NearestExemplar):
    def __init__(self, technique, exemplar_file):
        self.actual_exemplars = None
        super(TheoreticalStatisticalExemplar, self).__init__(technique, exemplar_file)

    def classify(self, painting, experience):
        if self.actual_exemplars == None:
            self.actual_exemplars = self.exemplars
            self.generate_exemplars([painting] + experience)
        return super(TheoreticalStatisticalExemplar, self).classify(painting, self.actual_exemplars)

    def generate_exemplars(self,data):
        self.exemplars = {}
        years = {}
        for painting in data:
            if painting.year not in years:
                years[painting.year] = []
            years[painting.year].append(painting)
        for year in years:
            centroid_data = self.centroid(years[year])
            centroid = FakePainting(-1, "", "Statistcal Centriod", year)
            centroid.data = centroid_data
            self.exemplars[year] = centroid

    def centroid(self, data):
        return self.technique.centroid(data)

class RealStatisticalExemplar(TheoreticalStatisticalExemplar):
    def centroid(self, data):
        centroid = super(RealStatisticalExemplar, self).centroid(data)
        nearest = data[0]
        dist = self.technique.distance(centroid, nearest.data)
        for i in data:
            new_dist = self.technique.distance(centroid, i.data)
            if new_dist < dist:
                dist = new_dist
                nearest = i
        
        print "Statistical Exemplar for {}: {}\nArtistical Exemplar: {}\n".format(nearest.year, nearest.title, self.actual_exemplars[int(nearest.year)].title if int(nearest.year) in self.actual_exemplars else "N/A")
        return nearest.data
            
