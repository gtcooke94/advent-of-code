from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter


def soln_a(data):
    parsed_data = parse(data)
    soln = 0
    for group in parsed_data:
        group_set = set()
        for person in group:
            group_set |= set(person)
        soln += len(group_set)

    return soln


def soln_b(data):
    parsed_data = parse(data)
    soln = 0
    for group in parsed_data:
        group_set = set("abcdefghijklmnopqrstuvwxyz")
        for person in group:
            group_set &= set(person)
        soln += len(group_set)

    return soln


def parse(data):
    groups = data.split("\n\n")
    parsed_groups = [group.split("\n") for group in groups]
    return parsed_groups


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=6)
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
