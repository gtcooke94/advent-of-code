from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter


def soln_a(data):
    parsed_data = parse(data)
    return max(determine_location_value(seat_loc) for seat_loc in parsed_data)


def determine_location_value(seat_loc):
    front_back = seat_loc[:7]
    left_right = seat_loc[7:]
    cur_front_back = [0, 127]
    for char in front_back:
        if char == "F":
            cur_front_back = [cur_front_back[0], sum(cur_front_back) // 2]
        else:
            cur_front_back = [sum(cur_front_back) // 2 + 1, cur_front_back[1]]
    cur_left_right = [0, 7]
    for char in left_right:
        if char == "L":
            cur_left_right = [cur_left_right[0], sum(cur_left_right) // 2]
        else:
            cur_left_right = [sum(cur_left_right) // 2 + 1, cur_left_right[1]]
    final_row = cur_front_back[0]
    final_col = cur_left_right[0]
    return final_row * 8 + final_col


def soln_b(data):
    parsed_data = parse(data)
    seat_locs = set(determine_location_value(seat_loc) for seat_loc in parsed_data)
    all_seats = [[row, col] for row in range(1, 127) for col in range(0, 8)]
    potential_locs = set(row * 8 + col for row, col in all_seats)
    ans = potential_locs - seat_locs
    for loc in ans:
        if loc - 1 in seat_locs and loc + 1 in seat_locs:
            return loc


def parse(data):
    yield from data.split("\n")


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=5)
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
