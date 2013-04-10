import kyffin.techniques.technique_factory as techniqueFactory
import kyffin.gui.guiFactory as guiFactory
import kyffin.ml.mlFactory as mlFactory

from analyser import Analyser
from optparse import OptionParser 
import unittest

VERSION_FILE = 'VERSION.txt'

def main():
    """Main entry method to the Kyffin project."""
    (options, args) = parse()

    if options.test_flag:
        from kyffin.test.statistical_test import StatisticalTest
        suite = unittest.TestLoader().loadTestsFromTestCase(StatisticalTest)
        unittest.TextTestRunner(verbosity=2).run(suite)
    else :
#        print "Kyffin ({0})".format(loadVersion())
        if options.csv is not None:
            tech = techniqueFactory.getTechnique(options.technique)
            gui = guiFactory.getGUI(options.gui, options.technique)
            ml = mlFactory.getML(options.ml, tech)
            analyser = Analyser(tech, gui, ml, options.five_flag, options.export_path, options.classify)
            analyser.run(options.csv)
        else:
            raise BaseException('No data file specified')

def parse():
    parser = OptionParser()
    parser.add_option('-t', '--test', default=False, action='store_true', dest='test_flag', help='Run tests and nothing else.')
    parser.add_option('-a', '--technique', default='rgb', dest='technique', help='Set Technique type.')
    parser.add_option("-d", "--csv", dest="csv", help="Analyse CSV file.", metavar="CSV")
    parser.add_option('-g', '--gui', dest='gui', help='Set GUI type (defaults to text-based.')
    parser.add_option('-m', '--ml', dest='ml', help='Set Machine Learning type (defaults to kNN.')
    parser.add_option('-5', '--bin-years', dest='five_flag', default=False, action='store_true', help='Bin paintings into years of five.')
    parser.add_option('-e', '--export', dest='export_path', default=False, help='Export analysed data to a file.')
    parser.add_option('-c', '--classify', dest='classify', default=None, help='Painting to Classify.')
    return parser.parse_args()

def loadVersion():
    """Loads Version information from the file defined by VERSION_FILE"""
    version = 'Unkown Version'
    try:
        with open(VERSION_FILE, 'r') as vFile:
            version = vFile.readline().rstrip('\n')
    except IOError as e:
        print "Unable to load version file: {0}\nReason: {1}".format(VERSION_FILE, e)
    return version
