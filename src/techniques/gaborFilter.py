from math import cos, sin, exp, pow, pi, ceil

import numpy, cv

class GaborFilter:

	def gabor(self, x, y, sigmaX, sigmaY, theta, gLambda, psi, gamma):
		thetaX = x * cos(theta) + y * sin(theta)
		thetaY = -(x * sin(theta)) + y * cos(theta)

		return exp(-0.5*(pow(thetaX,2)/pow(sigmaX,2)+pow(thetaY,2)/pow(sigmaY,2))) * cos(2*pi/gLambda*thetaX+psi)

	# From wikipedia's MATLAB code.
	def getFilter(self, sigma, theta, gLambda, psi, gamma):
		sigmaX = sigma
		sigmaY = sigma/gamma

		# Bounding box
		nstds = 3
		xMax = max(abs(nstds * sigmaX * cos(theta)), abs(nstds * sigmaY * sin(theta)))
		xMax = ceil(max(1, xMax))

		yMax = max(abs(nstds * sigmaX * sin(theta)), abs(nstds * sigmaY * cos(theta)))
		yMax = ceil(max(1, yMax))

		xMin = -xMax
		yMin = -yMax

		x,y = numpy.meshgrid(range(xMin, xMax), range(yMin, yMax))

		yDim = len(range(xMin, xMax))
		xDim = len(range(yMin, yMax))

		print x
		print xDim
		print yDim

		result = numpy.zeros(shape=(xDim, yDim))

		for i in range(xDim):
			for j in range(yDim):
				curX = x[i,j]
				curY = y[i,j]
				result[i,j] = self.gabor(x[i,j], y[i,j], sigmaX, sigmaY, theta, gLambda, psi, gamma)
			

		return result

if __name__ == '__main__':
	g = GaborFilter()
	gabor = g.getFilter(1.0,0,1.0,0,10.0)
	print gabor
	gFilter = cv.fromarray(gabor)
	src = cv.LoadImageM('data/nlw_nlw_gcf05061_large.jpg', cv.CV_LOAD_IMAGE_GRAYSCALE)

	cv.ShowImage('', src)
	cv.WaitKey(0)

	
	cv.Filter2D(src, src, gFilter)

	cv.ShowImage('',src)


	cv.WaitKey(0)
