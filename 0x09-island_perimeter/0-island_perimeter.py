'''
Create a function def island_perimeter(grid):
that returns the perimeter of the island described in grid:

- grid is a list of list of integers:
  - 0 represents water
  - 1 represents land
  - Each cell is square, with a side length of 1
  - Cells are connected horizontally/vertically (not diagonally).
  - grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesnt have “lakes” (water inside that isnt connected
  to the water surrounding the island).
'''


def island_perimeter(grid):
    '''
    Calculater the perimeter of the grid
    '''
    perimeter = 0
    h = len(grid)
    w = len(grid[0])
    for i in range(0, h):
        for j in range(0, w):
            'if current square is a 1 or land'
            if grid[i][j] == 1:
                'if upper row is in range'
                if i - 1 >= 0:
                    'if upper square is water'
                    if grid[i - 1][j] == 0:
                        perimeter += 1
                'if lower roe is in range'
                if i + 1 < h:
                    'if lower square is water'
                    if grid[i + 1][j] == 0:
                        perimeter += 1
                'if previous column is in range'
                if j - 1 >= 0:
                    'if previous square is water'
                    if grid[i][j - 1] == 0:
                        perimeter += 1
                'if next column is in range'
                if j + 1 < w:
                    'if next square is water'
                    if grid[i][j + 1] == 0:
                        perimeter += 1
    return perimeter
