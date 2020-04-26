#!/usr/bin/env python3
from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter


imp = ImageProcessor()
cf = ColorFilter()

arr = imp.load("../resources/elon_musk.jpg")
#arr = cf.invert(arr)
#arr = cf.to_blue(arr)
#arr = cf.to_green(arr)
#arr = cf.to_red(arr)
#arr = cf.celluloid(arr)
arr = cf.to_grayscale(arr, 'w')
imp.display(arr)
