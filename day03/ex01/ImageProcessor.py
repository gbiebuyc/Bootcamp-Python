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

# i = ImageProcessor()
# im = i.load('../resources/42AI.png')
# i.display(im)

