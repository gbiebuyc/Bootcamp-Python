import pandas as pd

def proportionBySport(df, year, sport, gender):
    df = df[df['Year'] == year]
    df = df[df['Sex'] == gender]
    df = df.drop_duplicates('Name')
    total = df.shape[0]
    df = df[df['Sport'] == sport]
    return df.shape[0] / total


