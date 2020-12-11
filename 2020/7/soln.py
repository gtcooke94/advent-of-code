from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter
from collections import defaultdict
from collections import deque


def soln_a(data):
    parsed_data = parse(data)
    reversed_graph = defaultdict(list)
    for d in parsed_data:
        container = list(d.keys())[0]
        contains = list(d[container].keys())
        for held in contains:
            reversed_graph[held].append(container)

    goldbag = "shiny gold bag"
    q = deque()
    q.append(goldbag)
    counter = -1
    visited = set()
    while q:
        bag = q.popleft()
        if bag in visited:
            continue
        visited.add(bag)
        counter += 1
        can_hold = reversed_graph[bag]
        for color in can_hold:
            q.append(color)

    return counter


def soln_b(data):
    parsed_data = parse(data)
    forward_graph = defaultdict(list)
    for d in parsed_data:
        container = list(d.keys())[0]
        contains = d[container]
        forward_graph[container] = contains

    goldbag = "shiny gold bag"
    q = deque()
    q.append((goldbag, 1, 1))
    counter = 0
    while q:
        bag, value, num_parent_bags = q.popleft()
        num_this_bag = value * num_parent_bags
        counter += num_this_bag
        can_hold = forward_graph[bag]
        for color, value in can_hold.items():
            q.append((color, value, num_this_bag))

    return counter - 1  # minus 1 gold bag


def parse(data):
    """light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags."""
    data = data.strip("\n")
    for line in data.split("\n"):
        container, rest = line.split(" contain ")
        container = container[:-1]  # remove plural
        contains = {}
        for item in rest.split(", "):
            value, kind = item.split(" ", 1)
            kind = kind.strip(".")
            if value == "no":
                continue
            value = int(value)
            if value > 1:
                kind = kind[:-1]  # remove plural
            contains[kind] = value
        yield {container: contains}

    return data
    # return data or yield data


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=7)
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
