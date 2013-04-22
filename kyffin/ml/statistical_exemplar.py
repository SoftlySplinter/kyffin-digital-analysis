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
#        error = {stat: self.technique.distance(self.exemplars[stat].data, self.actual_exemplars[real].data) for (stat, real) in zip(self.exemplars, self.actual_exemplars)}
#        error = {stat: (self.exemplars[real].year, self.actual_exemplars[real].year) for real in self.actual_exemplars}
        error = {}
        for year in self.exemplars:
            if int(year) in self.actual_exemplars:
                error[year] = self.technique.distance(self.exemplars[year].data, self.actual_exemplars[int(year)].data)
        print "\nError distance: {}".format(sum(error.values()))
        fig = plot.figure(4)
        ax = fig.add_subplot(111)
        errors = [error[key] for key in sorted(error)]
        ax.bar(range(len(error)), errors)
        ax.set_xticklabels( sorted(error) )
        plot.ylabel('Error Distance')
        plot.xlabel('Year')
        plot.show()

        for y,e in zip(sorted(error), errors):
            print str(y) + " " + str(e)

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
#        s = ""
#        s += str(nearest.year) + "\t"
#        s += str(nearest.id)
#        if int(nearest.year) in self.actual_exemplars:
#            s += "\t" + str(self.actual_exemplars[int(nearest.year)].id)
#        else:
#            s += "\tN/A"
#        s += "\t" + str(len(data))
#        print s
        return (nearest.data, nearest.id)
