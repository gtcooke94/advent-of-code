from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter


def soln_a(data):
    parsed_data = parse(data)
    sorted_chargers = sorted(parsed_data)
    sorted_chargers.append(sorted_chargers[-1] + 3)
    sorted_chargers = [0] + sorted_chargers
    differences = Counter()
    for i in range(len(sorted_chargers) - 1):
        differences[(sorted_chargers[i + 1] - sorted_chargers[i])] += 1

    return differences[1] * differences[3]


def soln_b(data):
    parsed_data = parse(data)
    sorted_chargers = sorted(parsed_data)
    sorted_chargers.append(sorted_chargers[-1] + 3)
    sorted_chargers = [0] + sorted_chargers
    total_branches_dp = [1] * len(sorted_chargers)
    for i in range(len(sorted_chargers)):
        if i == 0:
            continue
        branches = 0
        for lookback in range(1, 4):
            potential_link = i - lookback
            if potential_link < 0:
                continue
            if sorted_chargers[i] - sorted_chargers[potential_link] > 3:
                continue
            branches += total_branches_dp[potential_link]
        total_branches_dp[i] = branches

    return total_branches_dp[-1]


def parse(data):
    """16
    10
    15
    5
    1
    11
    7
    19
    6
    12
    4
    """
    return (int(line) for line in data.split("\n"))
    # return data or yield data


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=10)
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
