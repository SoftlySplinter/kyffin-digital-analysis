#! /usr/bin/env python

import unittest

import sys
sys.path.append('../src/')

import cv
import statistical

class StatisticalTest(unittest.TestCase):
	data = []
	def setUp(self):
		for r in range(0, 255, 32):
			for b in range(0, 255, 32):
				for g in range(0, 255, 32):
					self.data.append(cv.RGB(r,g,b))

	def testAverageRGB(self):
		for rgb in self.data:
			testMat = cv.CreateMat(10, 10, cv.CV_32SC4)
			cv.Set(testMat, rgb)
			self.assertEqual(rgb, statistical.AverageRGB(testMat))

if __name__ == '__main__':
    unittest.main()
