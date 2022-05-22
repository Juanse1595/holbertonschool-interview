#!/usr/bin/python3
import sys


def queens(n, i, a, b, c):
    '''
    Calculates every possible solution to the n queen puzzle
    '''
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from queens(n, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        yield a


if sys.argv.__len__() != 2:
    print('Usage: nqueens N ')
    sys.exit(1)

n = int(sys.argv[1])
if not isinstance(n, int):
    print('N must be a number')
    sys.exit(1)

if n < 4:
    print('N must be at least 4')
    sys.exit(1)

for y_coordinates in queens(n, 0, [], [], []):
    x_coordinates = [[x] for x in range(0, n)]
    for i, x in enumerate(x_coordinates):
        x.append(y_coordinates[i])
    print(x_coordinates)
