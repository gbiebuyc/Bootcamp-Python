import pandas as pd

class FileLoader:
    def load(self, path):
        data = pd.read_csv(path)
        print('Loading dataset of dimensions %d x %d' % data.shape)
        return data

