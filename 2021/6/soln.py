from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter
import os
from laternfish import LanternFish, counter_solution
from matrix_solution import matrix_solve


def soln_a_brute(data):
    initial_timers = parse(data)
    lantern_fish = [LanternFish(initial_timer) for initial_timer in initial_timers]
    for _ in range(79):
        lantern_fish_to_add = []
        for fish in lantern_fish:
            maybe_new_fish = fish.step()
            if maybe_new_fish:
                lantern_fish_to_add.append(maybe_new_fish)
        lantern_fish.extend(lantern_fish_to_add)
    return len(lantern_fish)

def soln_a(data):
    initial_timers = parse(data)
    # return counter_solution(initial_timers, 80)
    return matrix_solve(initial_timers, 80)


def soln_b(data):
    initial_timers = parse(data)
    # return counter_solution(initial_timers, 80)
    return matrix_solve(initial_timers, 256)


def parse(data):
    numbers = [int(n) for n in data.split(",")]
    return numbers
    # return data or yield data


def solve_puzzle(soln, a_or_b):
    day = int(os.path.basename(os.getcwd()))
    puzzle = Puzzle(year=2021, day=day)
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
