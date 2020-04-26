#!/usr/bin/env python3
from FileLoader import FileLoader
from ProportionBySport import proportionBySport

loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')
print(proportionBySport(data, 2004, 'Tennis', 'F'))
