#! /usr/bin/env python

import csv
import kyffin.painting as paint
import random, re
import matplotlib.pyplot as plot
import os.path
import logging
import scipy.stats as stats
import math

DATA_DIR = 'data/'

class Analyser:
    def __init__(self, technique, gui, ml, fiveYearBins, export_path):
        self.technique = technique
        self.gui = gui
        self.ml = ml
        self.fiveYearBins = fiveYearBins
        self.export_path = export_path
        
        self.paintings = []

    def run(self, data):
        self.loadPaintings( data )
        self.analyse()

        if self.export_path: return

        self.gui.render(self.paintings)

        actual = []
        classified = []

        for i in range(len(self.paintings)):
            self.classify(i, actual, classified)

        (correlation, unknown) = self.correlation(classified, actual)
        print 'Correlation: {0} ({1})'.format(correlation, unknown)

        plot.figure(2)
        plot.plot(actual, classified, 'x')
        plot.xlabel('Actual Year')
        plot.ylabel('Classified Year')
        plot.show()

    def classify(self, i, actual, classified):
        toClassify = self.paintings.pop(i)
        actualY = toClassify.year
        classifiedY = self.ml.classify( toClassify, self.paintings )
        self.paintings.insert(i, toClassify)
        if classifiedY == -1:
            return


        actual.append(actualY)
        classified.append(classifiedY)

    def correlation(self, classified, actual):
        a = [float(x) for x in classified]
        b = [float(x) for x in actual]
        return stats.pearsonr(a, b)

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
