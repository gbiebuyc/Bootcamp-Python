#!/usr/bin/env python3

class CsvReader():
    def __init__(self, file_name, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.file_obj = open(file_name, 'r')
        self.header = []
        self.data = []
        nb_columns = None
        for line in self.file_obj:
            row = [x.strip().strip('"') for x in line.strip().strip(sep).split(sep)]
            if nb_columns is None:
                nb_columns = len(row)
            if nb_columns != len(row):
                self.data = None
                return
            self.data.append(row)
        if header:
            self.header = self.data.pop(0)
    
    def __enter__(self):
        if self.data is None:
            return None
        return self
    
    def __exit__(self, type, value, traceback):
        self.file_obj.close()

    def getdata(self):
        return self.data

    def getheader(self):
        return self.header


if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
    with CsvReader('bad.csv') as file:
        if file == None:
            print("File is corrupted")
