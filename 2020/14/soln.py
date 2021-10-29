from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter
from DockingMemory import DockingMemory, MaskOperation, AssignOperation, MASK, ASSIGN, DockingMemory2



def soln_a(data):
    parsed_data = parse(data)
    docking_memory = DockingMemory()
    for op in parsed_data:
        docking_memory.do_operation(op)

    return docking_memory.sum_memory()


def soln_b(data):
    parsed_data = parse(data)
    docking_memory = DockingMemory2()
    for op in parsed_data:
        docking_memory.do_operation(op)

    return docking_memory.sum_memory()


def parse(data):
    for line in data.split("\n"):
        if line.startswith(MASK):
            # do something
            op = MaskOperation(line.split("=")[1])
        else:
            # it's a memory line
            op = AssignOperation(line)
        yield op
    # return data or yield data


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=14)
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
