#!/usr/bin/env python3
import sys

string = ' '.join(sys.argv[1:])
string = string[::-1]
string = string.swapcase()
print(string)
