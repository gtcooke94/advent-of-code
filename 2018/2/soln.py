from aocd.models import Puzzle
import inputs
import sys
from collections import Counter


def soln_a(data):
    box_ids = parse(data)
    twos = 0
    threes = 0
    for box_id in box_ids:
        letter_counts = Counter(box_id)
        counts = set(letter_counts.values())
        twos += 2 in counts
        threes += 3 in counts
    return twos * threes


def soln_b(data):
    box_ids = parse(data)
    for start, box_id1 in enumerate(box_ids):
        for box_id2 in box_ids[start+1:]:
            differences = 0
            for i in range(len(box_id1)):
                if box_id1[i] != box_id2[i]:
                    differences += 1
                if differences > 1:
                    break
            if differences == 1:
                different_idx = None
                for i in range(len(box_id1)):
                    if box_id1[i] != box_id2[i]:
                        different_idx = i
                        break
                return box_id1[:different_idx] + box_id1[different_idx+1:]

        
        
def parse(data):
    return data.split("\n")

def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2018, day=2)
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
