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

#    def to_grayscale(self, arr, filter="w"):
#        if filter == 'm' or filter == 'mean':
#            shape = arr.shape
#            grey = np.sum(arr, axis=2) / 3
#            print(grey.shape)
#            arr = np.broadcast_to(grey, shape)
#            print(arr.shape)
#            #return np.mean(arr, axis=2)
#        if filter == 'w' or filter == 'weighted':
#            return np.dot(arr[...,:3], [0.299, 0.587, 0.114])


imp = ImageProcessor()
cf = ColorFilter()

arr = imp.load("../resources/elon_musk.jpg")
#arr = cf.invert(arr)
#arr = cf.to_blue(arr)
#arr = cf.to_green(arr)
#arr = cf.to_red(arr)
arr = cf.celluloid(arr)
imp.display(arr)
