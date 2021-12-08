from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter
import os
from bingo import BingoBoard

def soln_a(data):
    numbers, boards = parse(data)
    for number in numbers:
        for board in boards:
            board.number_called(number)
            if board.check_winning():
                return board.calculate_solution(number)

def soln_b(data):
    numbers, boards = parse(data)
    for number in numbers:
        i = 0
        while i < len(boards):
            board = boards[i]
            board.number_called(number)
            if board.check_winning():
                if len(boards) == 1:
                    return board.calculate_solution(number)
                del boards[i]
            else:
                i += 1


    return soln


def parse(data):
    numbers, rest = data.split("\n\n", 1)
    numbers = [int(i) for i in numbers.split(",")]
    boards = []
    for grid in rest.split("\n\n"):
        # No separator makes python split on whitespace
        boards.append(BingoBoard.from_string(grid, None))
    return numbers, boards
    # return data or yield data


def solve_puzzle(soln, a_or_b):
    day = int(os.path.basename(os.getcwd()))
    puzzle = Puzzle(year=2021, day=day)
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
