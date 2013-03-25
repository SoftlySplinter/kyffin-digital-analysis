from kyffin.techniques.statistical import RGBAnalysis
from kyffin.techniques.statistical import HSVAnalysis
from kyffin.techniques.histogram import HistogramAnalysis, HSVHistogramAnalysis
from kyffin.techniques.edge_orientation import EdgeOrientation
from kyffin.techniques.hog import *
from kyffin.techniques.ensemble import Ensemble

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
        return HOG() 
    elif name == "rhog":
        return SimpleRHOG() 
    elif "+" in name:
        technique_names = name.split('+')
        techniques = [getTechnique(technique_name) for technique_name in technique_names]
        return Ensemble(*techniques)
    else:
        raise Exception('Unknown technique {0}'.format(name))
