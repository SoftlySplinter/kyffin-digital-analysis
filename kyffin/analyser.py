#! /usr/bin/env python

import csv
import kyffin.painting as paint
import random, re
import os.path
import logging
import math

DATA_DIR = 'data/'

class Fake:
    def __init__(self, path):
        self.id = -1
        self.filePath = path
        self.data = None

class Analyser:
    def __init__(self, technique, gui, ml, fiveYearBins, export_path, classify):
        self.technique = technique
        self.gui = gui
        self.ml = ml
        self.fiveYearBins = fiveYearBins
        self.export_path = export_path
        self.to_classify = classify
        
        self.paintings = []

    def run(self, data):
        self.loadPaintings( data )
        self.analyse()

        if self.export_path: return

        self.gui.render(self.paintings)

        actual = []
        classified = []

        if self.to_classify == None:
            for i in xrange(len(self.paintings)):
                self.classify(i, actual, classified)
            self.ml.visualise(actual, classified)
        else:
            temp = Fake(self.to_classify)
            temp.data = self.technique.analyse(Fake(self.to_classify))
            print "Classified as: {}".format(self.ml.classify(temp, self.paintings))

    def classify(self, i, actual, classified):
        toClassify = self.paintings.pop(i)
        actualY = toClassify.year
        classifiedY = self.ml.classify( toClassify, self.paintings )
        self.paintings.insert(i, toClassify)
        if classifiedY == -1:
            return
        actual.append(actualY)
        classified.append(classifiedY)

    def analyse(self):
        for painting in self.paintings:
            painting.data = self.technique.analyse(painting)
        if self.export_path:
            with open(self.export_path, 'w') as export_file:
                export_file.write(self.technique.export(self.paintings))

    def loadPaintings( self, data ):
        with open( data, 'r' ) as csvFile:
            dataReader = csv.reader(csvFile, delimiter=',', quotechar='"')
            for row in dataReader:
                try:
                    painting = paint.load(row, DATA_DIR)
                    if re.match('^\d\d\d\d$', painting.year):
                        if self.fiveYearBins:
                            painting.year = math.floor(int(painting.year)/5) * 5
                        self.paintings.append(painting)
                except IOError:
                    continue
