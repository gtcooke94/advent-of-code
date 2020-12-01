from aocd.models import Puzzle
import inputs
import sys
from collections import Counter


def soln_a(data):
    data = parse(data)
    # Brute force grossness
    #  for i, item in enumerate(data):
    #      for other in data[i+1:]:
    #          if item + other == 2020:
    #              return item * other
    numbers = set(data)
    for number in numbers:
        needed = 2020 - number
        if needed in numbers:
            return number * needed


def soln_b(data):
    data = parse(data)
    number_pairs = set()
    numbers = set(data)
    for i, num1 in enumerate(data):
        for num2 in data[i + 1:]:
            number_pairs.add((num1, num2))
    for p1, p2 in number_pairs:
        needed = 2020 - (p1 + p2)
        if needed in numbers:
            return p1 * p2 * needed


def parse(data):
    data = [int(i) for i in data.split("\n")]
    return data


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
