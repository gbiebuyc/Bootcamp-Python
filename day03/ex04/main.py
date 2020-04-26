#!/usr/bin/env python3
from ImageProcessor import ImageProcessor
from AdvancedFilter import AdvancedFilter


imp = ImageProcessor()
af = AdvancedFilter()

arr = imp.load("../resources/elon_musk.jpg")
arr = af.mean_blur(arr)
imp.display(arr)
