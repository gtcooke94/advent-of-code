from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter


def soln_a(data):
    parsed_data = parse(data)
    increased = 0
    for i in range(len(parsed_data) - 1):
        increased += parsed_data[i+1] > parsed_data[i]

    return increased


def soln_b(data):
    parsed_data = parse(data)
    sliding_sums = []
    for i in range(len(parsed_data) - 2):
        sliding_sum = parsed_data[i] + parsed_data[i + 1] + parsed_data[i + 2]
        sliding_sums.append(sliding_sum)

    increased = 0
    for i in range(len(sliding_sums) - 1):
        increased += sliding_sums[i+1] > sliding_sums[i]

    return increased


def parse(data):
    return [int(line) for line in data.split("\n")]


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2021, day=1)
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
