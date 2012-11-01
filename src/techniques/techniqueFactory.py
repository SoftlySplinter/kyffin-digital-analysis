from statistical import StatisticalAnalysis
from histogram import HistogramAnalysis

def getTechnique(name):
	if name == 'rgb':
		return StatisticalAnalysis()
	elif name == 'histogram':
		return HistogramAnalysis([50,50,50])
	else:
		raise Exception('Unknown technique {0}'.format(name))
