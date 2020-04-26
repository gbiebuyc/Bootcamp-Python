import pandas as pd

class FileLoader:
    def load(self, path):
        df = pd.read_csv(path)
        print('Loading dataset of dimensions %d x %d' % df.shape)
        return df

    def display(self, df, n):
        if n > 0:
            print(df.head(n))
        else:
            print(df.tail(-n))

