import pandas as pd
import matplotlib.pyplot as plt

class MyPlotLib:
    def histogram(self, df, features):
        if type(features) not in (list, tuple):
            raise Exception('features must be a list or tuple')
        for feature in features:
            x = df[feature].tolist()
            plt.hist(x, bins=20)
            plt.show()
