from aocd.models import Puzzle
import inputs
import sys

# import personal_aoc_helpers as pah
from collections import Counter
import os

NUMS = set(("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"))
# WORDS = set(("one", "two", "three", "four", "five", "six", "seven", "eight", "nine"))
WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def soln_a(data):
    parsed_data = parse(data)
    sum = 0
    first_digit = None
    second_digit = None
    for entry in parsed_data:
        for e in entry:
            if e in NUMS:
                first_digit = int(e)
                break
        for e in entry[::-1]:
            if e in NUMS:
                second_digit = int(e)
                break
        sum += first_digit * 10 + second_digit
    return sum


def soln_b(data):
    parsed_data = parse(data)
    parsed_data = parse(data)
    sum = 0
    first_digit = None
    second_digit = None
    for entry in parsed_data:
        for i in range(len(entry)):
            if d := determine_digit(entry, i):
                first_digit = d
                break
        for i in range(len(entry) - 1, -1, -1):
            if d := determine_digit(entry, i):
                second_digit = d
                break
        sum += first_digit * 10 + second_digit
    return sum


def determine_digit(entry, i):
    if entry[i] in NUMS:
        return int(entry[i])
    # 3, 4, and 5 letter combos could match WORDS
    # Prefix tree is probably the best here but lets brute force first
    try:
        if entry[i:i+3] in WORDS:
            return WORDS[entry[i:i+3]]
        elif entry[i:i+4] in WORDS:
            return WORDS[entry[i:i+4]]
        if entry[i:i+5] in WORDS:
            return WORDS[entry[i:i+5]]
    except IndexError:
        return


def parse(data):
    return (line for line in data.split("\n"))


def solve_puzzle(soln, a_or_b):
    day = int(os.path.basename(os.getcwd()))
    puzzle = Puzzle(year=2023, day=day)
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
