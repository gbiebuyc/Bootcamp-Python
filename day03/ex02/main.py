#!/usr/bin/env python3
from ImageProcessor import ImageProcessor
from ScrapBooker import ScrapBooker


imp = ImageProcessor()
sb = ScrapBooker()

arr = imp.load("../resources/42AI.png")
print('size before:', arr.shape)
# arr = sb.thin(arr, 3, 1)
# arr = sb.crop(arr, (80, 80), (50, 50))
# arr = sb.crop(arr, (800, 80), (50, 50))
# arr = sb.juxtapose(arr, 3, 1)
arr = sb.mosaic(arr, (2, 4))
print('size after: ', arr.shape)
imp.display(arr)

