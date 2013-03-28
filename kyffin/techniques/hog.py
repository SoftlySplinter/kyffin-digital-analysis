import cv, numpy, math, cv2
from kyffin.techniques import Technique
import os


class BaseHOG( Technique ):
    def __init__(self, bins):
        self.bins = bins

    def analyse(self, painting):
        # Normalise colour and gamma (not needed)
#        img = self.normalize_gamma(cv.LoadImageM(painting.filePath, cv.CV_LOAD_IMAGE_GRAYSCALE), 1)
        img = cv2.imread(painting.filePath)
        # Compute gradients
        return self.compute_gradients(img)


    @classmethod
    def normalize_gamma(cls, img, gamma):
        out = cv.CreateMat(img.rows, img.cols, img.type)
        cv.Pow(img, out, gamma)
        cv.ConvertScaleAbs(out, out)
        return out

    @classmethod
    def compute_gradients(cls, img):
        gradient_filter_x = numpy.ones((3,1), numpy.float32)

        gradient_filter_x[0][0] = -1
        gradient_filter_x[1][0] = 0
        gradient_filter_x[2][0] = 1

        gradient_filter_y = numpy.ones((1,3), numpy.float32)

        gradient_filter_y[0][0] = -1
        gradient_filter_y[0][1] = 0
        gradient_filter_y[0][2] = 1

        dst_x = cv2.filter2D(img, -1, gradient_filter_x)
        dst_y = cv2.filter2D(img, -1, gradient_filter_y)

        dst = numpy.zeros(img.shape, numpy.float32)

        w,h,_ = img.shape
        for x in range(w):
            for y in range(h):
                x_c = dst_x[x][y]
                y_c = dst_y[x][y]
                x_co = max(x_c)
                y_co = max(y_c)
                dst[x][y] = math.atan2(x_co, y_co)

        return dst

class HOG(BaseHOG):
    def __init__(self, bins):
        super(HOG, self).__init__(bins)
        self.path = ".hog"

    """Basic HOG."""
    def analyse(self, painting):
        if not self.exists(painting.id):
            gradients = super(HOG, self).analyse(painting)
            self.can(painting.id, gradients)
        else:
            gradients = self.uncan(painting.id)
        return cv2.calcHist([gradients], [0], None, [self.bins], [0, 2 * math.pi])

    def exists(self, id):
        return os.path.exists("{}/{}.npy".format(self.path, str(id)))

    def can(self, id, data):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        filename="{}/{}".format(self.path, str(id))
        numpy.save(filename, data)

    def uncan(self, id):
        filename="{}/{}.npy".format(self.path, str(id))
        return numpy.load(filename)

class SimpleRHOG(BaseHOG):
    """Rectangulary celled HOG. This is far too basic, inefficient and 
    decreases performance."""
    def analyse(self, painting):
        data = super(SimpleRHOG, self).analyse(painting)
        segmented = numpy.ones((10,10), numpy.float32)
        for i in range(1,10):
            for j in range(1,10):
                avg = 0
                for x in range(1,int(data.rows / 10)):
                    for y in range(1,int(data.cols / 10)):
                        (val, _, _, _) = cv.Get2D(data, x*i, y*j)
                        avg += val
                avg /= int(data.rows/10) * int(data.cols / 10)
                segmented[i-1][j-1] = avg
        
        
        segs = cv.fromarray(segmented) 
        grad_img = cv.CreateImage((segs.rows, segs.cols), cv.IPL_DEPTH_32F, segs.channels)
        cv.Convert(segs, grad_img)
        hist = cv.CreateHist([15], cv.CV_HIST_ARRAY, [[0, 2 * math.pi]])
        cv.CalcHist([grad_img], hist)
        return hist

    def distance(self, current, other):
        return cv.CompareHist(current,other,cv.CV_COMP_CHISQR)

    def export(self, data, year):
        with NamedTemporaryFile() as temp:
            cv.Save(temp.name, data.bins, name=year)
            output = ""
            for line in temp:
                output += line
        return output
