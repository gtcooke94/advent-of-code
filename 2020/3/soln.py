from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter
from functools import reduce


def soln_a(data):
    grid, num_rows, num_cols = parse(data)
    #  pah.print_grid(grid)
    num_trees = traverse_slope(grid, num_rows, num_cols, 3, 1)
    return num_trees


def traverse_slope(grid, num_rows, num_cols, xslope, yslope):
    """
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    """
    cur_row = 0
    cur_col = 0
    num_trees = 0
    # Access grid at col % num_cols because it repeats right infinitely
    while cur_row < num_rows:
        is_tree = grid[(cur_row, cur_col % (num_cols))] == "#"
        num_trees += is_tree
        cur_row += yslope
        cur_col += xslope
    return num_trees


def soln_b(data):
    grid, num_rows, num_cols = parse(data)
    num_trees = [
        traverse_slope(grid, num_rows, num_cols, 1, 1),
        traverse_slope(grid, num_rows, num_cols, 3, 1),
        traverse_slope(grid, num_rows, num_cols, 5, 1),
        traverse_slope(grid, num_rows, num_cols, 7, 1),
        traverse_slope(grid, num_rows, num_cols, 1, 2),
    ]

    return reduce(lambda x, y: x * y, num_trees)


def parse(data):
    grid = dict()
    row = None
    col = None
    for row, line in enumerate(data.split("\n")):
        for col, character in enumerate(line):
            grid[(row, col)] = character
    return grid, row + 1, col + 1


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=3)
    answer = soln(puzzle.input_data)
    print(answer)
    if a_or_b == "a":
        puzzle.answer_a = answer
    else:
        puzzle.answer_b = answer


if __name__ == "__main__":
    a_or_b = sys.argv[1]
    soln = soln_a if a_or_b == "a" else soln_b
    inp = sys.argv[2]
    if inp == "solve":
        solve_puzzle(soln, a_or_b)
    else:
        data = inputs.inputs[int(inp)]
        print(soln(data))
