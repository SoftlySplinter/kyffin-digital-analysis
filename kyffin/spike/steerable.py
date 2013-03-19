import cv2, numpy, sys

filter000 = numpy.array([[1.,0.,-1.],[1.,0.,-1.],[1.,0.,-1.]], dtype=numpy.float32)
filter045 = numpy.array([[0.,-1.,-1.],[1.,0.,-1.],[1.,1.,0.]], dtype=numpy.float32)
filter090 = numpy.array([[1.,1.,1.],[0.,0.,0.],[-1.,-1.,-1.,]], dtype=numpy.float32)
filter135 = numpy.array([[1.,1.,0.],[1.,0.,-1.],[0.,-1.,-1.]], dtype=numpy.float32)
print filter

image = cv2.imread(sys.argv[1], cv2.CV_LOAD_IMAGE_GRAYSCALE)

i000 = cv2.filter2D(image, -1, filter000)
i045 = cv2.filter2D(image, -1, filter045)
i090 = cv2.filter2D(image, -1, filter090)
i135 = cv2.filter2D(image, -1, filter135)

cv2.imshow("Filtered 000", i000)
cv2.imshow("Filtered 045", i045)
cv2.imshow("Filtered 090", i090)
cv2.imshow("Filtered 135", i135)
cv2.waitKey()


