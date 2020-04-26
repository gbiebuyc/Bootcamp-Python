#!/usr/bin/env python3
import numpy as np
from PIL import Image

class ImageProcessor:
    def load(self, path):
        im = Image.open(path)
        width, height = im.size
        print('Loading image of dimensions %d x %d' % (width, height))
        array = np.array(im, dtype=np.float32)
        array /= 255
        return array

    def display(self, array):
        array *= 255
        array = array.astype(np.uint8)
        im = Image.fromarray(array)
        im.show()


class ColorFilter:
    def invert(self, arr):
        return arr * -1 + 1.0

    def to_blue(self, arr):
        arr[:, :, 0] = 0
        arr[:, :, 1] = 0
        return arr

    def to_green(self, arr):
        return arr * np.array((0, 1, 0))

    def to_red(self, arr):
        #return arr - self.to_blue(arr) - self.to_green(arr)
        return arr * np.array((1, 0, 0))

    def celluloid(self, arr, num_tresholds=4):
        arr *= num_tresholds
        arr = arr.astype(np.int8)
        arr = arr.astype(np.float32)
        arr /= num_tresholds
        return arr

    def to_grayscale(self, arr, filter="w"):
        if filter == 'm' or filter == 'mean':
            shape = arr.shape
            arr = np.sum(arr, axis=2, keepdims=True) / 3
            arr = np.broadcast_to(arr, shape)
            return 1 * arr
        if filter == 'w' or filter == 'weighted':
            arr *= [0.299, 0.587, 0.114]
            arr = np.sum(arr, axis=2, keepdims=True)
            arr = np.tile(arr, (1, 1, 3))
            return arr


# imp = ImageProcessor()
# cf = ColorFilter()
# 
# arr = imp.load("../resources/elon_musk.jpg")
# #arr = cf.invert(arr)
# #arr = cf.to_blue(arr)
# #arr = cf.to_green(arr)
# #arr = cf.to_red(arr)
# #arr = cf.celluloid(arr)
# arr = cf.to_grayscale(arr, 'w')
# imp.display(arr)
