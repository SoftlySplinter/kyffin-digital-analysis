"""Classified based on the nearest exemplar."""
import csv
from kyffin.ml.knn import KNearestNeighbour
from kyffin.ml import ML
import sys

class FakePainting:
    def __init__(self, id, filename, title, year):
        self.filePath = 'data/' + filename
        self.title = title
        self.year = year
        self.data = None
        self.id = id

class NearestExemplar(ML):
    def __init__(self, technique, exemplar_file):
        self.technique = technique
        self.exemplars = {}
        self.read_exemplars(exemplar_file)

    def read_exemplars(self, db):
        with open(db, 'r') as csv_file:
            for row in csv.reader(csv_file, delimiter=',', quotechar='"'):
                try:
                    r_filename      = row[0]
                    r_id            = row[1]
                    r_title         = row[2]
                    r_exemplar_year = int(row[4])
                    temp = FakePainting(r_id, r_filename, r_title, r_exemplar_year)
                    temp.data = self.technique.analyse(temp)
                    self.exemplars[temp.year] = temp
                except ValueError as e:
                    continue

    def classify(self, painting, experience):
        """Classify the point in space"""
        nearest_exemplar = None
        for year in self.exemplars:
            if self.exemplars[year].id == painting.id:
                continue
            distance = self.technique.distance(painting.data, self.exemplars[year].data)
            if nearest_exemplar == None or nearest_exemplar['distance'] > distance:
                nearest_exemplar = {'year': year, 'distance': distance}
            
        return nearest_exemplar['year']
