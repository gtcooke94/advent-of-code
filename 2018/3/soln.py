from aocd.models import Puzzle
import inputs
import sys
from collections import defaultdict


def soln_a(data):
    data = parse(data)
    grid = defaultdict(int)
    for left_edge, top_edge, width, height in data:
        widths = range(left_edge, left_edge + width)
        heights = range(top_edge, top_edge + height)
        for w in widths:
            for h in heights:
                grid[(w, h)] += 1
    return sum(1 for i in grid.values() if i >= 2)
        


def soln_b(data):
    data = parse_b(data)
    data = list(data)
    grid = {}
    for claim_id, left_edge, top_edge, width, height in data:
        widths = range(left_edge, left_edge + width)
        heights = range(top_edge, top_edge + height)
        for w in widths:
            for h in heights:
                if (w, h) in grid.keys():
                    grid[(w,h)] = "X"
                else:
                    grid[(w,h)] = claim_id
    for claim_id, left_edge, top_edge, width, height in data:
        widths = range(left_edge, left_edge + width)
        heights = range(top_edge, top_edge + height)
        not_correct = False
        for w in widths:
            if not_correct:
                break
            for h in heights:
                if grid[(w, h)] == "X":
                    not_correct = True
                    break
        if not not_correct:
            return claim_id[1:]

                


def parse(data):
    """
    1 @ 1,3: 4x4
    2 @ 3,1: 4x4
    3 @ 5,5: 2x2
    """
    lines = data.split("\n")
    for line in lines:
        _, remaining = line.split("@")
        left, right = remaining.split(":")
        left_edge, top_edge = (int(i) for i in left.split(","))
        width, height = (int(i) for i in right.split("x"))
        yield left_edge, top_edge, width, height

def parse_b(data):
    """
    1 @ 1,3: 4x4
    2 @ 3,1: 4x4
    3 @ 5,5: 2x2
    """
    lines = data.split("\n")
    for line in lines:
        claim_id, remaining = line.split("@")
        left, right = remaining.split(":")
        left_edge, top_edge = (int(i) for i in left.split(","))
        width, height = (int(i) for i in right.split("x"))
        yield claim_id, left_edge, top_edge, width, height




def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2018, day=3)
    answer = soln(puzzle.input_data)
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
