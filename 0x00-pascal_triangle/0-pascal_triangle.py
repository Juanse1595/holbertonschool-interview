#!/usr/bin/python3
'''
Create a function that returns a list of lists of
integers representing the Pascals triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
'''


def pascal_triangle(n):
    '''
    Generates an array that emulates a pascal
    '''
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(n - 1):
        temp = [0] + triangle[-1] + [0]
        row = []
        for j in range(len(triangle[-1] + 1)):
            row.append(temp[j] + temp[j + 1])
        triangle.append(row)
    return triangle
