"""Classified based on the nearest exemplar."""
import csv
from kyffin.ml.knn import KNearestNeighbour
import sys

class FakePainting:
    def __init__(self, id, filename, title, year):
        self.filePath = 'data/' + filename
        self.title = title
        self.year = year
        self.data = None
        self.id = id

class StatisticalExemplar:
    def __init__(self, technique, exemplar_file):
        self.technique = technique
        self.exemplars = {}
        self.read_exemplars(exemplar_file)
        self.statistical_exemplars = None

    def read_exemplars(self, db):
        with open(db, 'r') as csv_file:
            for row in csv.reader(csv_file, delimiter=',', quotechar='"'):
                try:
                    r_filename      = row[0]
                    r_id            = row[1]
                    r_title         = row[2]
                    r_exemplar_year = row[4]
                    temp = FakePainting(r_id, r_filename, r_title, r_exemplar_year)
                    temp.data = self.technique.analyse(temp)
                    self.exemplars[temp.year] = temp
                except ValueError as e:
                    continue

    def classify(self, painting, experience):
        """Classify the point in space"""
        if self.statistical_exemplars == None:
            self.generate_exemplars([painting]+experience)
        in_exemplars = False
        for exemplar in self.exemplars:
            if self.exemplars[exemplar].id == painting.id:
                artistic = self.exemplars[exemplar]
                statistical = self.statistical_exemplars[exemplar]
                return self.technique.distance(artistic.data, statistical.data)
        return -1

    def generate_exemplars(self,data):
        self.statistical_exemplars = {}
        years = {}
        for painting in data:
            if painting.year not in years:
                years[painting.year] = []
            years[painting.year].append(painting)
        for year in years:
            centroid_data = self.technique.centroid(years[year])
            centroid = FakePainting(-1, "", "Statistcal Centriod", year)
            centroid.data = centroid_data
            self.statistical_exemplars[year] = centroid
