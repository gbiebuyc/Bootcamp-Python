#!/usr/bin/env python3
import sys

def operations(n, m):
    print('Sum:        ', n+m)
    print('Difference: ', n-m)
    print('Product:    ', n*m)
    print('Quotient:   ', 'ERROR (div by zero)' if m == 0 else n/m)
    print('Remainder:  ', 'ERROR (modulo by zero)' if m == 0 else n%m)

def print_usage():
    print('Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3')
    sys.exit()

if len(sys.argv) > 3:
    print('InputError: too many arguments\n')
if len(sys.argv) != 3:
    print_usage()

try:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
except:
    print('InputError: only numbers\n')
    print_usage()

operations(n, m)
