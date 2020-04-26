#!/usr/bin/env python3
from FileLoader import FileLoader
from HowManyMedals import howManyMedals

loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')
print(howManyMedals(data, 'Kjetil Andr Aamodt'))
