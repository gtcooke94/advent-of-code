from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter


def soln_a(data):
    parsed_data = parse(data)
    num_valid = 0
    for low, high, letter, string in parsed_data:
        is_valid = low <= Counter(string)[letter] <= high
        num_valid += is_valid

    return num_valid


def soln_b(data):
    parsed_data = parse(data)
    num_valid = 0
    for low, high, letter, string in parsed_data:
        lowidx = low - 1
        highidx = high - 1
        if lowidx >= len(string):
            continue
        if highidx >= len(string):
            is_valid = string[lowidx] == letter
        else:
            is_valid = (string[lowidx] == letter) ^ (string[highidx] == letter)
        num_valid += is_valid

    return num_valid


def parse(data):
    for line in data.split("\n"):
        number, rest = line.split(" ", 1)
        low, high = (int(i) for i in number.split("-"))
        letter, rest = rest.split(":")
        string = rest.strip(" ")
        string = string.strip("\n")
        yield low, high, letter, string


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=2)
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
