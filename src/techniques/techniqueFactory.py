from statistical import RGBAnalysis
from statistical import HSVAnalysis
from histogram import HistogramAnalysis

def getTechnique(name):
	if name == 'rgb':
		return RGBAnalysis()
	if name == 'hsv':
		return HSVAnalysis()
	elif name == 'histogram':
		return HistogramAnalysis([5,5,5])
	else:
		raise Exception('Unknown technique {0}'.format(name))
