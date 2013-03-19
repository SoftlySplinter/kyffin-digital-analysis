import cv2, numpy, sys

def thresh(data):
    threshed = 0
    count = 0
    for row in data:
        for point in row:
            count+=1
            if point > 25:
                threshed+=1
    return float(threshed)/float(count)

filter000 = numpy.array([[1.,0.,-1.],[1.,0.,-1.],[1.,0.,-1.]], dtype=numpy.float32)
filter135 = numpy.array([[0.,-1.,-1.],[1.,0.,-1.],[1.,1.,0.]], dtype=numpy.float32)
filter090 = numpy.array([[1.,1.,1.],[0.,0.,0.],[-1.,-1.,-1.,]], dtype=numpy.float32)
filter045 = numpy.array([[1.,1.,0.],[1.,0.,-1.],[0.,-1.,-1.]], dtype=numpy.float32)

image = cv2.imread(sys.argv[1], cv2.CV_LOAD_IMAGE_GRAYSCALE)

i000 = cv2.filter2D(image, -1, filter000)
i045 = cv2.filter2D(image, -1, filter045)
i090 = cv2.filter2D(image, -1, filter090)
i135 = cv2.filter2D(image, -1, filter135)

m000 = thresh(i000)
m045 = thresh(i045)
m090 = thresh(i090)
m135 = thresh(i135)

print "0: {}\n45: {}\n90: {}\n135: {}".format(int(m000*100), int(m045*100), int(m090*100), int(m135*100))

