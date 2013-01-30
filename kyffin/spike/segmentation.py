import cv

PATH = "data/nlw_nlw_kwf00003_large.jpg"

img = cv.LoadImageM(PATH)
hsv = cv.CloneMat(img)
cv.CvtColor(img, hsv, cv.CV_RGB2HSV)

cv.ShowImage("original", img)
cv.ShowImage("hsv", hsv)
cv.WaitKey(0)

mask = cv.CreateMat(img.rows, img.cols, cv.CV_8U)

pt = cv.Get2D(hsv, 25, 50)
cv.InRangeS(hsv, pt, cv.Scalar(255,255,255, 0), mask)

cv.ShowImage("mask", mask)
cv.WaitKey(0)
