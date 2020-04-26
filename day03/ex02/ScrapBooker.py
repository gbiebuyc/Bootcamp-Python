import numpy as np

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
        return np.tile(arr, dimensions + (1,))
