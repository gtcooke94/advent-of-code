from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter
from ship import Ship

directions = ["N", "E", "S", "W"]

def soln_a(data):
    # Assume you can only turn in multiples of 90
    parsed_data = list(parse(data))
    current_direction_int = 1 
    x = 0
    y = 0
    for entry in parsed_data:
        current_direction = directions[current_direction_int]
        move_direction, distance = entry
        distance = int(distance)
        if move_direction == "F":
            move_direction = current_direction
        elif move_direction == "R":
            number = distance // 90
            current_direction_int = (current_direction_int + number) % 4
        elif move_direction == "L":
            number = distance // 90
            current_direction_int = (current_direction_int - number) % 4

        if move_direction == "N":
            y += distance
        elif move_direction == "S":
            y -= distance
        elif move_direction == "E":
            x += distance
        elif move_direction == "W":
            x -= distance

    return abs(x) + abs(y)

def soln_b(data):
    parsed_data = parse(data)
    ship = Ship()
    for entry in parsed_data:
        move_direction, number = entry
        number = int(number)
        ship.move(move_direction, number)

    return ship.manhatten_distance() 


def parse(data):
    for line in data.split("\n"):
        yield (line[0], line[1:])
    # return data or yield data


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=12)
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
