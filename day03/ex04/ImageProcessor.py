import numpy as np
from PIL import Image

class ImageProcessor:
    def load(self, path):
        im = Image.open(path)
        print('Loading image of dimensions %d x %d' % im.size)
        array = np.array(im, dtype=np.float32)
        array /= 255
        return array

    def display(self, array):
        array *= 255
        array = array.astype(np.uint8)
        im = Image.fromarray(array)
        im.show()
