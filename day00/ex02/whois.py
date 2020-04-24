#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    sys.exit()
try:
    n = int(sys.argv[1])
except:
    print('ERROR')
    sys.exit()
if n == 0:
    print("I'm Zero.")
elif n%2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")

