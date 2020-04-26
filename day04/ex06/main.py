#!/usr/bin/env python3
from FileLoader import FileLoader
from MyPlotLib import MyPlotLib

loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')
mpl = MyPlotLib()
mpl.histogram(data, ('Age',))
