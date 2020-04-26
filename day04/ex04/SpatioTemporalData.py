import pandas as pd

class SpatioTemporalData:
    def __init__(self, df):
        self.df = df

    def when(self, location):
        df = self.df[self.df['City'] == location]
        year_list = df['Year'].unique().tolist()
        return year_list

    def where(self, date):
        df = self.df[self.df['Year'] == date]
        city_list = df['City'].unique().tolist()
        return city_list

