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


class AdvancedFilter:
    def mean_blur(self, arr, kernel_size=9):
        ret = np.zeros(arr.shape, arr.dtype)
        half_ker_sz = kernel_size//2
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                p1 = (max(0, i - half_ker_sz), max(0, j - half_ker_sz))
                p2 = (min(arr.shape[0], i + half_ker_sz), min(arr.shape[1], j + half_ker_sz))
                kernel = arr[p1[0]:p2[0], p1[1]:p2[1]].reshape(-1, 3)
                ret[i][j] = np.sum(kernel, axis=0) / kernel.shape[0]
        return ret


# imp = ImageProcessor()
# af = AdvancedFilter()
# 
# arr = imp.load("../resources/elon_musk.jpg")
# arr = af.mean_blur(arr)
# imp.display(arr)
