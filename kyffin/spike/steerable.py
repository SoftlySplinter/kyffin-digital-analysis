import cv2, numpy, sys

def thresh(data):
    threshed = 0
    count = 0
    for row in data:
        for point in row:
            count+=1
            if point < 255/2:
                threshed+=1
    return float(threshed)/float(count)*100

filter000 = numpy.array([[0.,0.,1.,0.,0.],[0.,0.,1.,0.,0.],[0.,0.,1.,0.,0.],[0.,0.,1.,0.,0.],[0.,0.,1.,0.,0.]], dtype=numpy.float32)
filter135 = numpy.array([[1.,0.,0.,0.,0.],[0.,1.,0.,0.,0.],[0.,0.,1.,0.,0.],[0.,0.,0.,1.,0.],[0.,0.,0.,0.,1.]], dtype=numpy.float32)
filter090 = numpy.array([[0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.],[1.,1.,1.,1.,1.],[0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.]], dtype=numpy.float32)
filter045 = numpy.array([[0.,0.,0.,0.,1.],[0.,0.,0.,1.,0.],[0.,0.,1.,0.,0.],[0.,1.,0.,0.,0.],[1.,0.,0.,0.,0.]], dtype=numpy.float32)

image = cv2.imread(sys.argv[1])

i000 = [cv2.filter2D(chan, -1, filter000) for chan in cv2.split(image)]
i045 = [cv2.filter2D(chan, -1, filter045) for chan in cv2.split(image)]
i090 = [cv2.filter2D(chan, -1, filter090) for chan in cv2.split(image)]
i135 = [cv2.filter2D(chan, -1, filter135) for chan in cv2.split(image)]


#rgb = ["r","g","b"]
#for (name,im) in [("0",i000), ("45",i045), ("90",i090), ("135",i135)]:
#    i = 0
#    for c in im:
#        cv2.imshow(name + rgb[i], c)
#        i+= 1
#cv2.waitKey(0)

m000 = [thresh(i) for i in i000]
m045 = [thresh(i) for i in i045]
m090 = [thresh(i) for i in i090]
m135 = [thresh(i) for i in i135]

print "0: {}\n45: {}\n90: {}\n135: {}".format(m000, m045, m090, m135)

