from kyffin.techniques.statistical import RGBAnalysis
from kyffin.techniques.statistical import HSVAnalysis
from kyffin.techniques.histogram import HistogramAnalysis
from kyffin.techniques.edge_orientation import EdgeOrientation
from kyffin.techniques.colour_hog import ColourEdgeHistogramAnalysis
from kyffin.techniques.hog import HistogramOfOrientationGradients
from kyffin.techniques.ensemble import Ensemble

def getTechnique(name):
    if name == 'rgb':
        return RGBAnalysis()
    if name == 'hsv':
        return HSVAnalysis()
    elif name == 'histogram':
        return HistogramAnalysis([5,5,5])
    elif name == 'edge-orientation':
        return EdgeOrientation()
    elif name == "hog":
        return HistogramOfOrientationGradients()
    elif "+" in name:
        technique_names = name.split('+')
        techniques = [getTechnique(technique_name) for technique_name in technique_names]
        return Ensemble(*techniques)
    else:
        raise Exception('Unknown technique {0}'.format(name))
