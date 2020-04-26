import pandas as pd

def youngestFellah(df, year):
    print(df.shape)
    df = df[df['Year'] == '2004']
    print(df.shape)

