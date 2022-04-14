#!/usr/bin/python3
'''
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
'''
def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = []
    row = 1
    while row <= n:
        if row == 1:
            triangle.append([1])
        elif row == 2:
            triangle.append([1, 1])
        else:
            new_array = [1]
            idx_aux = 0
        while idx_aux + 1 < row - 1:
            new_array.append([triangle[row - 2][idx_aux] + triangle[row - 2][idx_aux + 1]])
            idx_aux = idx_aux + 1
        new_array.append([1])
        triangle.append([new_array])
        