#!/usr/bin/env python3
from FileLoader import FileLoader
from SpatioTemporalData import SpatioTemporalData

loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')
sp = SpatioTemporalData(data)
print(sp.where(1896))
print(sp.where(2016))
print(sp.when('Athina'))
print(sp.when('Paris'))
