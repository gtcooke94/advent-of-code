from aocd.models import Puzzle
import inputs
import sys
from collections import Counter


def soln_a(data):
    pass
    # return answer


def soln_b(data):
    pass
    # return answer


def parse(data):
    pass
    # return data or yield data


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=1)
    answer = soln(puzzle.input_data)
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
