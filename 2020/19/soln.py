from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter
from copy import deepcopy
from solna import follows_rule
from solnb import follows_rule_b

def soln_a(data):
    rules, messages = parse(data)
    print(rules)
    print(messages)
    count = 0
    for message in messages:
        print("====")
        print(message)
        follows, remaining_message = follows_rule(rules, 0, message)
        print(follows, remaining_message)
        follows &= len(remaining_message) == 0
        print(follows)
        print("====")
        count += follows
    return count


def soln_b(data):
    """
    Is soln_a but with the following replaced, which creates loops in the rules
    8: 42 | 42 8
    11: 42 31 | 42 11 31
    """
    rules, messages = parse(data)
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    # print(rules)
    # print(messages)
    count = 0
    for message in messages:
        # print("====")
        # print(message)
        follows, remaining_message = follows_rule_b(rules, 0, message, 0, len(message))
        # print(follows, remaining_message)
        follows &= len(remaining_message) == 0
        # print(follows)
        # print("====")
        count += follows
    return count


def parse(data):
    raw_rules, data = data.split("\n\n")
    rules = {}
    for line in raw_rules.split("\n"):
        rule_number, content = line.split(": ")
        if content.startswith('"'):
            # "a" or "b"
            rules[int(rule_number)] = content[1]
        else:
            content = parse_rule_content(content)
            rules[int(rule_number)] = content

    messages = data.split("\n")

    return rules, messages
    # return data or yield data

def parse_rule_content(content):
    if "|" in content:
        rule1, rule2 = content.strip().split("|")
        rule_links1 = [int(i) for i in rule1.strip().split(" ")]
        rule_links2 = [int(i) for i in rule2.strip().split(" ")]
        return [rule_links1, rule_links2]
    else:
        return [[int(i) for i in content.split(" ")]]
    
    


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=19)
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