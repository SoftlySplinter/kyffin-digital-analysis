from kyffin.techniques.statistical import RGBAnalysis
from kyffin.techniques.statistical import HSVAnalysis
from kyffin.techniques.histogram import HistogramAnalysis, HSVHistogramAnalysis
from kyffin.techniques.edge_orientation import EdgeOrientation
from kyffin.techniques.hog import *
from kyffin.techniques.ensemble import Ensemble
from kyffin.techniques.steerable_filter import SteerableFilter
from kyffin.techniques.gabor_filter import GaborFilter
from kyffin.techniques.size import Size
from math import pi

def getTechnique(name):
    if name == 'rgb':
        return RGBAnalysis()
    if name == 'hsv':
        return HSVAnalysis()
    elif name == 'hist':
        return HistogramAnalysis()
    elif name == 'hsv-hist':
        return HSVHistogramAnalysis()
    elif name == 'edge':
        return EdgeOrientation()
    elif name == "hog":
        return HOG(4)
    elif name == "hog8":
        return HOG(8)
    elif name == "hog16":
        return HOG(16)
    elif name == "rhog":
        return SimpleRHOG() 
    elif name == "steerable":
        return SteerableFilter()
    elif name == "gabor":
        return GaborFilter([(i * pi) / 4 for i in xrange(1,4)])
    elif name == "gabor8":
        return GaborFilter([(i * pi) / 8 for i in xrange(1,8)])
    elif name == "gabor16":
        return GaborFilter([(i * pi) / 16 for i in xrange(1,16)])
    elif name == "size":
        return Size()
    elif "+" in name:
        technique_names = name.split('+')
        techniques = [getTechnique(technique_name) for technique_name in technique_names]
        return Ensemble(*techniques)
    else:
        raise Exception('Unknown technique {0}'.format(name))
