'''
Sudoku solver
Created by Jan Kammermayer
Email: Honza.Kammermayer@gmail.com

Setup with ->   python sudoku_solver.py sudoku.csv
                python sudoku_solver.py sudoku_easy.csv
                python sudoku_solver.py sudoku_hard.csv
'''

import csv
import copy
import random
import sys
# sys.setrecursionlimit(10000)

grid = []
counter = 0

def load_sudoku(name):
    '''
    Load and return sudoku from csv file
    '''
    with open(name) as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            lst = []
            for num in row:
                lst.append(int(num))
            grid.append(lst)
    return grid

def any_empty_cell(grid):
    '''
    Check if sudoku have some empty cell
    '''
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                return True
    return False

def valid(grid, r, c, val):
    '''
    Check if 'val' is in grid
    '''
    for x in range(9):
        if grid[x][c] == val:
            return False

    for y in range(9):
        if grid[r][y] == val:
            return False

    sector_x = (r // 3) * 3
    sector_y = (c // 3) * 3
    for x in range(3):
        for y in range(3):
            if grid[sector_x + x][sector_y + y] == val:
                return False
    return True

def find_posibilities(grid):
    '''
    Create all sudoku posibilities
    '''
    sudoku_posibilities = []
    for x in range(9):
        sudoku_posibilities.append([])
        for y in range(9):
            sudoku_posibilities[x].append([])
            if grid[x][y] == 0:
                for i in range(1, 10):
                    if valid(grid, x, y, i):
                        sudoku_posibilities[x][y].append(i)
    return sudoku_posibilities

def find_min_len(grid):
    '''
    Find cell with min len of posibilities [1-9]
    '''
    r, c, l = -1, -1, 9
    for x in range(9):
        for y in range(9):
            len_col = len(grid[x][y])
            if len_col < l and len_col != 0:
                r, c, l = x, y, len_col
    if r == -1:
        return -1, -1, -1
    return r, c, l

def print_sudoku(grid):
    '''
    Print sudoku
    '''
    print()
    for i, row in enumerate(grid):
        row = [x if x != 0 else '-' for x in row]
        print("| {} {} {} | {} {} {} | {} {} {} |".format(*row))
        if i % 3 == 2:
            print('-'*25)
    print()
    print('#'*25)

def solve_sudoku(grid):
    '''
    Sudoku solver init
    '''
    posibilities = find_posibilities(grid)
    x, y, l = find_min_len(posibilities)
    global counter
    if l == 1 and False:
        grid[x][y] = posibilities[x][y][0]
        solution = solve_sudoku(grid)
        counter += 1
        if not any_empty_cell(solution):
            return solution
    else:
        for i in posibilities[x][y]:
            temp = copy.deepcopy(grid)
            if valid(temp, x, y, i):
                temp[x][y] = i
                solution = solve_sudoku(temp)
                counter += 1
                if not any_empty_cell(solution):
                    return solution
    return grid

if __name__ == '__main__':
    if len(sys.argv) > 1:
        grid = load_sudoku(sys.argv[1])
        print_sudoku(grid)
        if input('Solve sudoku ? [y/n]: ') == 'y':
            solved_grid = solve_sudoku(grid)
            print_sudoku(solved_grid)
            # print(counter)
