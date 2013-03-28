"""Classified based on the nearest exemplar."""
import csv
from kyffin.ml.knn import KNearestNeighbour
from kyffin.ml.nearest_exemplar import NearestExemplar, FakePainting
import sys
import matplotlib.pyplot as plot
import numpy

class TheoreticalStatisticalExemplar(NearestExemplar):
    def __init__(self, technique, exemplar_file):
        self.actual_exemplars = None
        super(TheoreticalStatisticalExemplar, self).__init__(technique, exemplar_file)

    def classify(self, painting, experience):
        if self.actual_exemplars == None:
            self.actual_exemplars = self.exemplars
            self.generate_exemplars([painting] + experience)
#        if painting.id in [self.exemplars[e].id for e in self.exemplars]:
#            print painting.title + " in exemplars"
#            return -1
        return super(TheoreticalStatisticalExemplar, self).classify(painting, self.actual_exemplars)

    def generate_exemplars(self,data):
        self.exemplars = {}
        years = {}
        for painting in data:
            if painting.year not in years:
                years[painting.year] = []
            years[painting.year].append(painting)
        for year in years:
            (centroid_data, centroid_id) = self.centroid(years[year])
            centroid = FakePainting(centroid_id, "", "Statistcal Centriod", year)
            centroid.data = centroid_data
            self.exemplars[year] = centroid

    def centroid(self, data):
        return (self.technique.centroid(data), -1)

    def visualise(self, actual, classified):
        super(TheoreticalStatisticalExemplar, self).visualise(actual, classified)
        error = {stat: self.technique.distance(self.exemplars[stat].data, self.actual_exemplars[real].data) for (stat, real) in zip(self.exemplars, self.actual_exemplars)}
        print "\nError distance: {}".format(sum(error.values()))
        fig = plot.figure(4)
        ax = fig.add_subplot(111)
        errors = [error[key] for key in sorted(error)]
        ax.bar(range(len(error)), errors)
        ax.set_xticklabels( sorted(error) )
        plot.ylabel('Error Distance')
        plot.xlabel('Year')
        plot.show()

class RealStatisticalExemplar(TheoreticalStatisticalExemplar):
    def centroid(self, data):
        (centroid,_) = super(RealStatisticalExemplar, self).centroid(data)
        nearest = data[0]
        dist = self.technique.distance(centroid, nearest.data)
        for i in data:
            new_dist = self.technique.distance(centroid, i.data)
            if new_dist < dist:
                dist = new_dist
                nearest = i
        
        print "Statistical Exemplar for {}: {} ({})".format(
            nearest.year, 
            nearest.title, 
            nearest.id)
        if int(nearest.year) in self.actual_exemplars:
            if self.actual_exemplars[int(nearest.year)].id == nearest.id: 
                print "Artistical Exemplar matches ({})\n".format(len(data))
            else:
                print "Artistical Exemplar: {} ({}) ({})\n".format(
                   self.actual_exemplars[int(nearest.year)].title,
                   self.actual_exemplars[int(nearest.year)].id,
                   len(data))
        else:
            print "No artistical exemplar\n"
        return (nearest.data, nearest.id)
