from technique import Technique
import cv, numpy

class EdgeOrientation(Technique):
	DEFAULT = 'canny'
	def __init__(self, algorithm = DEFAULT):
		self.algorithm = algorithm

	def Analyse(self, painting):
		painting.data = self.edge(painting)

	def edge(self, painting):
		if self.algorithm == 'sobel':
			return self.sobelEdge(painting)
		elif self.algorithm == 'canny':
			return self.cannyEdge(painting)
		elif self.algorithm == 'scharr':
			return self.scharrEdge(painting)
		else:
			return self.sobelEdge(painting)

	def sobelEdge(self, painting):
		'''Perform Sobel Edge Detection.'''

		# Load the image.
		src = cv.LoadImageM(painting.filePath,cv.CV_LOAD_IMAGE_GRAYSCALE)

		# Sobel needs a 16-bit Signed value to prevent overflow.
		dst = cv.CreateMat(src.height, src.width, cv.CV_16S)

		# Smooth before performing.
		cv.Smooth(src, src, cv.CV_BLUR, 3, 3)

		# Perform Sobel.
		cv.Sobel(src, dst, 1, 1, 5)

		# Convert back to a 8-bit unsigned value for convenience.
		ret = cv.CreateMat(src.height, src.width, cv.CV_8U)
		cv.ConvertScaleAbs(dst,ret)

		return ret

	def cannyEdge(self, painting):
		'''Perform Canny Edge Detection.'''

		# Load the image.
		src = cv.LoadImageM(painting.filePath, cv.CV_LOAD_IMAGE_GRAYSCALE)

		# Canny needs the same type of destination.
		dst = cv.CreateMat(src.height, src.width, src.type)

		# Smooth before performing.
		cv.Smooth(src, src, cv.CV_BLUR, 3, 3)

		# Perform canny.
		cv.Canny(src, dst, 100.0, 200.0)

		return dst

	def scharrEdge(self, painting):
		'''Apply a Scharr Operator to the painting.
		
		To do this I've had to added the two different directions Scharr can work with (x 
		and y) using OpenCV's AddWeighted.'''

		# Load the image.
		src = cv.LoadImageM(painting.filePath, cv.CV_LOAD_IMAGE_GRAYSCALE)

		# Smooth before performing the edge detection.
		cv.Smooth(src, src, cv.CV_BLUR, 3, 3)

		# As Scharr uses Sobel in OpenCV, the destinations need to be 16-bit signed.
		dstX = cv.CreateMat(src.height, src.width, cv.CV_16S)
		dstY = cv.CreateMat(src.height, src.width, cv.CV_16S)

		# Perform Scharr in both axes.
		cv.Sobel(src, dstX, 1,0, cv.CV_SCHARR)
		cv.Sobel(src, dstY, 0,1, cv.CV_SCHARR)
		
		# Convert back to 8-bit unsigned
		retX = cv.CreateMat(src.height, src.width, cv.CV_8U)
		retY = cv.CreateMat(src.height, src.width, cv.CV_8U)

		cv.ConvertScaleAbs(dstX, retX)
		cv.ConvertScaleAbs(dstY, retY)

		# Add the two axes together equally.
		ret = cv.CreateMat(src.height, src.width, cv.CV_8U)
		cv.AddWeighted(retX, 0.5, retY, 0.5, 0, ret)

		return ret


	def distance(self, a, b):
		return 0
