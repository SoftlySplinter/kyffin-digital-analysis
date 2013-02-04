import cv, numpy, math
from kyffin.techniques import Technique


class BaseHOG( Technique ):
    def analyse(self, painting):
        # Normalise colour and gamma (not needed)
        img = self.normalize_gamma(cv.LoadImageM(painting.filePath, cv.CV_LOAD_IMAGE_GRAYSCALE), 1)

        # Compute gradients
        gradients = cv.fromarray(self.compute_gradients(img))
        return gradients


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

        kern_x = cv.fromarray(gradient_filter_x)
        kernel_x = cv.CreateMat(kern_x.rows, kern_x.cols, cv.CV_32F)
        cv.Convert(kern_x, kernel_x)

        kern_y = cv.fromarray(gradient_filter_y)
        kernel_y = cv.CreateMat(kern_y.rows, kern_y.cols, cv.CV_32F)
        cv.Convert(kern_y, kernel_y)

        dst_x = cv.CreateMat(img.rows, img.cols, img.type)
        dst_y = cv.CreateMat(img.rows, img.cols, img.type)
        cv.Filter2D(img, dst_x, kernel_x)
        cv.Filter2D(img, dst_y, kernel_y)

        dst = numpy.ones((img.rows, img.cols), numpy.float32)

        for x in range(img.rows):
            for y in range(img.cols):
                x_c = cv.Get2D(dst_x, x, y)
                y_c = cv.Get2D(dst_y, x, y)
                x_co = max(x_c)
                y_co = max(y_c)
                dst[x][y] = math.atan2(x_co, y_co)

        return dst

class HOG(BaseHOG):
    """Basic HOG."""
    def analyse(self, painting):
        gradients = super(HOG, self).analyse(painting)
        grad_img = cv.CreateImage((gradients.cols, gradients.rows), cv.IPL_DEPTH_32F, gradients.channels)
        cv.Convert(gradients, grad_img)
        hist = cv.CreateHist([15], cv.CV_HIST_ARRAY, [[0, 2 * math.pi]])
        cv.CalcHist([grad_img], hist)
        return hist

    def distance(self, current, other):
        return cv.CompareHist(current,other,cv.CV_COMP_CHISQR)
       

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
