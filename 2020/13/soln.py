from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from shuttle_search import ShuttleSearch

def soln_a(data):
    ss = ShuttleSearch(*parse_a(data))

    return ss.solve()


def soln_b(data):
    _, busses = parse_b(data)
    ss = ShuttleSearch(_, busses)

    return ss.solve_b()


def parse_a(data):
    line1, line2 = data.split("\n")
    arrival_time = int(line1)
    busses = [int(bus) for bus in line2.split(",") if bus != "x"]
    return arrival_time, busses
    # return data or yield data

def parse_b(data):
    line1, line2 = data.split("\n")
    arrival_time = int(line1)
    busses = [int(bus) if bus != "x" else bus for bus in line2.split(",")]
    return arrival_time, busses


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=13)
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
