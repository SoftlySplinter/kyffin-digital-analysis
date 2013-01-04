from kyffin.techniques.statistical import RGBAnalysis
from kyffin.techniques.statistical import HSVAnalysis
from kyffin.techniques.histogram import HistogramAnalysis
from kyffin.techniques.edge_orientation import EdgeOrientation
from kyffin.techniques.colour_hog import ColourEdgeHistogramAnalysis

def getTechnique(name):
    if name == 'rgb':
        return RGBAnalysis()
    if name == 'hsv':
        return HSVAnalysis()
    elif name == 'histogram':
        return HistogramAnalysis([5,5,5])
    elif name == 'edge-orientation':
        return EdgeOrientation()
    elif name == "colourhog":
        return ColourEdgeHistogramAnalysis()
    else:
        raise Exception('Unknown technique {0}'.format(name))
