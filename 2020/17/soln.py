from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter
from conway_cubes import ConwayCubes, ConwayCubes4D


def soln_a(data):
    parsed_data = parse(data)
    conway_cubes = ConwayCubes.from_string(data)
    for i in range(6):
        conway_cubes.simulate()

    return conway_cubes.total_active_cubes()


def soln_b(data):
    parsed_data = parse(data)
    conway_cubes = ConwayCubes4D.from_string(data)
    for i in range(6):
        conway_cubes.simulate()

    return conway_cubes.total_active_cubes()


def parse(data):
    return data
    # return data or yield data


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=17)
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
