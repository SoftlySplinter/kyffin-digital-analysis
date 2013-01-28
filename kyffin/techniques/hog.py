from kyffin.technique import Technique

class HistogramOfOrientationGradients( Technique ):
    def analyse(self, painting):
        # Normalise colour and gamma (not needed)
        img = self.normalize_gamma(cv.LoadImageM(painting.file_path), 1)

        # Compute gradients
        gradients = compute_gradients(img)

        # Weighted vote into spaital and orientation cells

        # Contrast normalise over overlapping spaital block

        # Collect HOG's over detection window

        # Linear SVM (probably not needed)

        pass

    def distance(self, current, other):
        return 0

    @classmethod
    def normalize_gamme(cls, img, gamma):
        out = cv.CreateMat(img.rows, img.cols, img.type)
        cv.Pow(img, out, gamma)
        cv.ConvertScaleAbs(out, out)
        return out

    @classmethod
    def compute_gradients(cls, img):
        pass