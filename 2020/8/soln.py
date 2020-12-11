from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter
from copy import deepcopy


def soln_a(data):
    instructions = parse(data)
    i = 0
    ops_done = set()
    accumulated = 0
    while i not in ops_done:
        operation, number = instructions[i]
        ops_done.add(i)
        if operation == "nop":
            i += 1
            continue
        elif operation == "acc":
            accumulated += number
            i += 1
        elif operation == "jmp":
            i += number
    return accumulated


def soln_b(data):
    instructions = parse(data)
    for j, (instruction, value) in enumerate(instructions):
        test_instructions = deepcopy(instructions)
        if instruction == "nop":
            test_instructions[j] = ("jmp", value)
        elif instruction == "jmp":
            test_instructions[j] = ("nop", value)
        i = 0
        ops_done = set()
        accumulated = 0
        while i not in ops_done and i != len(instructions):
            operation, number = test_instructions[i]
            ops_done.add(i)
            if operation == "nop":
                i += 1
                continue
            elif operation == "acc":
                accumulated += number
                i += 1
            elif operation == "jmp":
                i += number
        if i == len(instructions):
            return accumulated


def parse(data):
    """
    nop +0
    acc +1
    jmp +4
    acc +3
    jmp -3
    acc -99
    acc +1
    jmp -4
    acc +6
    """
    parsed_data = []
    for line in data.split("\n"):
        operation, number = line.split(" ")
        number = int(number)
        parsed_data.append((operation, number))

    return parsed_data


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=8)
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
