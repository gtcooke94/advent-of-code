from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter
import os
from hydrothermal_venture import GridWithLines


def soln_a(data):
    parsed_data = parse(data)
    grid = GridWithLines()
    for left, right in parsed_data:
        grid.mark_line_a(left, right)
    return grid.overlaps_count()


def soln_b(data):
    parsed_data = parse(data)
    grid = GridWithLines()
    for left, right in parsed_data:
        grid.mark_line_b(left, right)
    return grid.overlaps_count()


def parse(data):
    for line in data.split("\n"):
        left, right = line.split(" -> ")
        left = (int(i) for i in left.split(","))
        right = (int(i) for i in right.split(","))
        yield left, right
    # return data or yield data


def solve_puzzle(soln, a_or_b):
    day = int(os.path.basename(os.getcwd()))
    puzzle = Puzzle(year=2021, day=day)
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
