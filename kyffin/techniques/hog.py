import cv, numpy, math
from kyffin.techniques.technique import Technique

class HistogramOfOrientationGradients( Technique ):
    def analyse(self, painting):
        # Normalise colour and gamma (not needed)
        img = self.normalize_gamma(cv.LoadImageM(painting.filePath, cv.CV_LOAD_IMAGE_GRAYSCALE), 1)

        # Compute gradients
        gradients = self.compute_gradients(img)

        # Weighted vote into spaital and orientation cells

        # Contrast normalise over overlapping spaital block

        # Collect HOG's over detection window

        # Linear SVM (probably not needed)

        pass

    def distance(self, current, other):
        return 0

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

        cv.ShowImage("origin", img)
        cv.ShowImage("hog", cv.fromarray(dst))
        cv.WaitKey(0)
        return dst
