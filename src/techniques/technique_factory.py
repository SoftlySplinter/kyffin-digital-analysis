from statistical import RGBAnalysis
from statistical import HSVAnalysis
from histogram import HistogramAnalysis
from edge_orientation import EdgeOrientation

def getTechnique(name):
    if name == 'rgb':
        return RGBAnalysis()
    if name == 'hsv':
        return HSVAnalysis()
    elif name == 'histogram':
        return HistogramAnalysis([5,5,5])
    elif name == 'edge-orientation':
        return EdgeOrientation()
    else:
        raise Exception('Unknown technique {0}'.format(name))
