#!/usr/bin/env python3
from FileLoader import FileLoader
from YoungestFellah import youngestFellah

loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')
print(youngestFellah(data, 2004))
