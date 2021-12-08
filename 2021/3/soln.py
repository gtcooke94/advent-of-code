from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter
from copy import deepcopy

TIED = object()


def soln_a(data):
    parsed_data = parse(data)
    sums = [0 for _ in range(len(parsed_data[0]))]
    for line in parsed_data:
        for i, char in enumerate(line):
            sums[i] += 1 if char == "1" else -1
    binary = "".join("1" if s > 0 else "0" for s in sums)
    reversed = "".join("0" if s > 0 else "1" for s in sums)
    return int(binary, 2) * int(reversed, 2)


def soln_b(data):
    parsed_data = parse(data)
    oxygen = parsed_data
    co2 = deepcopy(parsed_data)
    for i in range(len(parsed_data[0])):
        if len(oxygen) > 1:
            sum_digit_oxygen = most_common_digit(line[i] for line in oxygen)
            sum_digit_oxygen = 1 if sum_digit_oxygen is TIED else sum_digit_oxygen
            oxygen = cut_list(oxygen, sum_digit_oxygen, i)
        if len(co2) > 1:
            sum_digit_co2 = most_common_digit(line[i] for line in co2)
            sum_digit_co2 = 0 if sum_digit_co2 is TIED else int(not sum_digit_co2)
            co2 = cut_list(co2, sum_digit_co2, i)
    return int(oxygen[0], 2) * int(co2[0], 2)

def cut_list(binaries, digit, position):
    return [b for b in binaries if b[position] == str(digit)]

def most_common_digit(digits):
    s = 0
    for digit in digits:
        s += 1 if digit == "1" else -1
    if s == 0:
        return TIED
    else:
        return int(s > 0)
        

def oxygen_generator(binaries):
    parsed_data = parse(data)
    sums = [0 for _ in range(len(parsed_data[0]))]
    for i in range(len(parsed_data[0])):
        for line in parsed_data:
            sums[i]




def parse(data):
    return [line for line in data.split("\n")]
    # return data or yield data


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2021, day=3)
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
