import cv, numpy
from kyffin.techniques.technique import Technique

class HistogramOfOrientationGradients( Technique ):
    def analyse(self, painting):
        # Normalise colour and gamma (not needed)
        img = self.normalize_gamma(cv.LoadImageM(painting.filePath), 1)

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
        gradient_filter = numpy.ones((3,1), numpy.float32)

        gradient_filter[0,0] = -1
        gradient_filter[1,0] = 0
        gradient_filter[2,0] = 1

        kern = cv.fromarray(gradient_filter)
        kernel = cv.CreateMat(kern.rows, kern.cols, cv.CV_32F)
        cv.Convert(kern, kernel)

        dst = cv.CreateMat(img.rows, img.cols, img.type)
        cv.Filter2D(img, dst, kernel)

        cv.ShowImage("origin", img)
        cv.ShowImage("filtered", dst)
        cv.WaitKey(0)
