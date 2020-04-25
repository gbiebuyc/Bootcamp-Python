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

class ScrapBooker:
    def crop(self, arr, dimensions, position=(0, 0)):
        p1 = position
        p2 = (p1[0]+dimensions[0], p1[1]+dimensions[1])
        w = arr.shape[1]
        h = arr.shape[0]
        if p2[0] > h or p2[1] > w:
            raise Exception('dimensions is larger than the current image size.')
        arr = arr[p1[0]:p2[0], p1[1]:p2[1]]
        return arr

    def thin(self, arr, n, axis):
        return np.delete(arr, range(0, arr.shape[axis], n), axis)

    def juxtapose(self, arr, n, axis):
        return np.concatenate((arr,)*n, axis)

    def mosaic(self, arr, dimensions):
        arr = self.juxtapose(arr, dimensions[0], 0)
        arr = self.juxtapose(arr, dimensions[1], 1)
        return arr


imp = ImageProcessor()
sb = ScrapBooker()

arr = imp.load("../resources/42AI.png")
print(arr.shape)
# arr = sb.thin(arr, 3, 1)
# arr = sb.crop(arr, (80, 80), (50, 50))
# arr = sb.crop(arr, (800, 80), (50, 50))
# arr = sb.juxtapose(arr, 3, 1)
arr = sb.mosaic(arr, (2, 4))
print(arr.shape)
imp.display(arr)

