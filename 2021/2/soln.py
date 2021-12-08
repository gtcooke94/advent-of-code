from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter

movements = {
    "forward": (1, 0),
    "down": (0, -1),
    "up": (0, 1),
}

def soln_a(data):
    pos = (0, 0)
    for movement, amount in parse(data):
        posx = pos[0] +  movements[movement][0] * amount
        posy = pos[1] + movements[movement][1] * amount
        pos = (posx, posy)

    return abs(pos[0] * pos[1])


def soln_b(data):
    pos = (0, 0)
    aim = 0
    for movement, amount in parse(data):
        if movement == "up":
            aim -= amount
        elif movement == "down":
            aim += amount
        else:
            posx = pos[0] + amount
            posy = pos[1] + amount * aim
            pos = (posx, posy)

    return abs(pos[0] * pos[1])


def parse(data):
    for line in data.split("\n"):
        movement, amount = line.strip().split(" ")
        yield movement, int(amount)
    return data
    # return data or yield data


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2021, day=2)
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
