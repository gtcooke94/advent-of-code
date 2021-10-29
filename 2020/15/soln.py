from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter, defaultdict
from better_solve import better_solve


def solve(nums, final_position):
    number_to_positions = defaultdict(list)
    for i, num in enumerate(nums):
        number_to_positions[num].append(i + 1)

    pos = len(nums) + 1
    # In my puzzle input, starting numbers aren't repeated, so after that we get a 0
    last_number = nums[-1]
    while pos <= final_position:
        current_number = 0
        if len(number_to_positions[last_number]) >= 2:
            current_number = number_to_positions[last_number][-1] - number_to_positions[last_number][-2]
        number_to_positions[current_number].append(pos)
        last_number = current_number
        pos += 1
        
    return last_number

def soln_a(data):
    return better_solve(parse(data), 2020)


def soln_b(data):
    return better_solve(parse(data), 30000000)


def parse(data):
    nums = list(int(i) for i in data.split(","))
    return nums
    # return data or yield data


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=15)
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
