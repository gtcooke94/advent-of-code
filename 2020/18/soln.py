from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter
from order_of_ops import addition_equal_with_multiplication, addition_before_multiplication


def soln_a(data):
    total = 0
    for expr in parse(data):
        total += addition_equal_with_multiplication(expr)
    return total


def soln_b(data):
    total = 0
    for expr in parse(data):
        total += addition_before_multiplication(expr)
    return total


def parse(data):
    for line in data.split("\n"):
        line = line.replace("(", "( ")
        line = line.replace(")", " )")
        yield line
    

    # return data or yield data


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=18)
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
