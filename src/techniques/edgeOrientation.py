from technique import Technique
import cv, numpy

class EdgeOrientation(Technique):
	DEFAULT = 'sobel'
	def __init__(self):
		self.algorithm = EdgeOrientation.DEFAULT

	def Analyse(self, painting):
		painting.data = self.edge(painting)

	def edge(self, painting):
		if self.algorithm == 'sobel':
			return self.sobelEdge(painting)
		else:
			return self.sobelEdge(painting)

	def sobelEdge(self, painting):
		src = cv.LoadImageM(painting.filePath,cv.CV_LOAD_IMAGE_GRAYSCALE)
		dst = cv.CreateMat(src.height, src.width, cv.CV_16S)
		cv.Sobel(src, dst, 1, 1, 3)
		return dst

	def distance(self, a, b):
		return 0


if __name__ == '__main__':
	src = cv.LoadImageM('test.png', cv.CV_LOAD_IMAGE_GRAYSCALE)
	dst = cv.CreateMat(src.height, src.width, cv.CV_16S)
	cv.Sobel(src, dst, 1,1)
	for x in range(dst.cols):
		for y in range(dst.rows):
			print dst[x,y],
		print ''
