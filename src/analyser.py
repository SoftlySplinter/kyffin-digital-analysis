#! /usr/bin/env python

'''
The runner class for the Kyffin program.

Author: Alexander Brown
'''

import csv
import painting as paint
import re
import matplotlib.pyplot as plot
import scipy.stats as stats
import math

DATA_DIR = 'data/'

class Analyser:
    '''
    A class to kick off analysis.
    '''

    def __init__(self, technique, gui, ml_tech, five_year_bins):
        '''
        Initialise the techniques, etc.
	'''
        self.technique = technique
        self.gui = gui
        self.ml_tech = ml_tech
        self.five_year_bins = five_year_bins
        
        self.paintings = []

    def run(self, data):
        '''Run the analyser.'''

        # Load the paintings and perform analysis
        self.load_paintings( data )
        self.analyse()

        # Render the GUI.
        self.gui.render(self.paintings)

        # Arrays to store actual and classified years
        actual = []
        classified = []

        # For each painting in the data set classify it.
        for i in range(len(self.paintings)):
            self.classify(i, actual, classified)

        # Perform correlation.
        (correlation, unknown) = self.correlation(classified, actual)
        print 'Correlation: {0} ({1})'.format(correlation, unknown)

        # Plot the graph.
        plot.figure(2)
        plot.plot(actual, classified, 'x')
        plot.xlabel('Actual Year')
        plot.ylabel('Classified Year')
        plot.show()

    def classify(self, i, actual, classified):
        '''Perform classifiction using the leave-one-out technique.'''

        # Remove the example from ther data set.
        to_classify = self.paintings.pop(i)

        # Take the actual year out of the example
        actual_year = to_classify.year

        # Perform classification.
        self.ml_tech.classify( to_classify, self.paintings )

        # Get the classified year.
        classified_year = to_classify.year

        # Reset the example and put it back into the data set.
        to_classify.year = actual_year
        self.paintings.insert(i, to_classify)

        # Add to the results.
        actual.append(actual_year)
        classified.append(classified_year)

    @staticmethod
    def correlation(classified, actual):
        '''Perform the correlation technique.'''
        cla = [float(x) for x in classified]
        act = [float(x) for x in actual]
        return stats.pearsonr(cla, act)

    def analyse(self):
        '''Analyse all paintings in the data set.'''
        for painting in self.paintings:
            self.technique.Analyse(painting)
        

    def load_paintings( self, data ):
        '''Load all paintings in the CSV file.'''

        # Open the CSV file
        with open( data, 'r' ) as csv_file:
            # Load as a CSV reader.
            data_reader = csv.reader(csv_file, delimiter=',', quotechar='"')

            # Iterate of the rows
            for row in data_reader:
                try:
                    # Load the painting but only include absolute years.
                    painting = paint.load(row, DATA_DIR)
                    if re.match('^\d\d\d\d$', painting.year):
                        # Perform 5-year binning.
                        if self.five_year_bins:
                            painting.year = math.floor(int(painting.year)/5) * 5
                        # Add the painting to the data set.
                        self.paintings.append(painting)
                except IOError:
                    continue
