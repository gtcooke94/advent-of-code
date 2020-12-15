from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter
from collections import deque


def soln_a(data):
    parsed_data = list(parse(data))
    len_preamble = 25
    valid_set = set()
    queue = deque(maxlen=len_preamble)
    queue.extend(parsed_data[:len_preamble])
    valid_set.update(parsed_data[:len_preamble])
    for num in parsed_data[len_preamble:]:
        works = False
        for a in valid_set:
            needed = num - a
            if needed == a:
                continue
            if needed in valid_set:
                works = True
                break
        to_remove = queue.popleft()
        valid_set.remove(to_remove)
        queue.append(num)
        valid_set.add(num)
        if not works:
            break

    return num


def soln_b(data):
    parsed_data = list(parse(data))
    bad_num = soln_a(data)
    i, j = 0, 0
    window_sum = parsed_data[i]
    while window_sum != bad_num:
        if window_sum > bad_num:
            window_sum -= parsed_data[i]
            i += 1
        if window_sum < bad_num:
            j += 1
            window_sum += parsed_data[j]

    return min(parsed_data[i : j + 1]) + max(parsed_data[i : j + 1])


def parse(data):
    for line in data.split("\n"):
        yield int(line)


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=9)
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
