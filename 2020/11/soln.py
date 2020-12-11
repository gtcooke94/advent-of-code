from aocd.models import Puzzle
import inputs
import sys
import personal_aoc_helpers as pah
from collections import Counter
from collections import deque
from copy import deepcopy


movements = [
    (0, 1),
    (1, 0),
    (1, 1),
    (0, -1),
    (-1, 0),
    (-1, -1),
    (-1, 1),
    (1, -1),
]


def soln_a(data):
    """
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
    Floor (.) never changes; seats don't move, and nobody sits on the floor.
    """
    grid = parse(data)
    new_grid = deepcopy(grid)
    grids_different = True

    while grids_different:
        for row in range(grid.num_rows):
            for col in range(grid.num_cols):
                if grid[row, col] == "L":
                    any_occupied = False
                    for drow, dcol in movements:
                        arow = row + drow
                        acol = col + dcol
                        if grid[arow, acol] == "#":
                            any_occupied = True
                            break
                    if not any_occupied:
                        new_grid[row, col] = "#"
                elif grid[row, col] == "#":
                    occupied = 0
                    for drow, dcol in movements:
                        arow = row + drow
                        acol = col + dcol
                        if grid[arow, acol] == "#":
                            occupied += 1
                        if occupied == 4:
                            new_grid[row, col] = "L"
                            break
        if grid == new_grid:
            break

        grid = new_grid
        new_grid = deepcopy(grid)
    occupied = 0
    for row in range(grid.num_rows):
        for col in range(grid.num_cols):
            if grid[row, col] == "#":
                occupied += 1
    return occupied


def soln_b(data):
    """
    As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!
    Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty seat below would see eight occupied seats:
    Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.
    """
    grid = parse(data)
    new_grid = deepcopy(grid)
    grids_different = True

    while grids_different:
        for row in range(grid.num_rows):
            for col in range(grid.num_cols):
                if grid[row, col] == "L":
                    any_occupied = False
                    for drow, dcol in movements:
                        if any_occupied:
                            break
                        arow = row + drow
                        acol = col + dcol
                        while grid[arow, acol] not in set(["#", "L", None]):
                            arow += drow
                            acol += dcol
                        if grid[arow, acol] == "#":
                            any_occupied = True
                            break
                    if not any_occupied:
                        new_grid[row, col] = "#"
                elif grid[row, col] == "#":
                    occupied = 0
                    for drow, dcol in movements:
                        if occupied == 5:
                            break
                        arow = row + drow
                        acol = col + dcol
                        while grid[arow, acol] not in set(["#", "L", None]):
                            arow += drow
                            acol += dcol
                        if grid[arow, acol] == "#":
                            occupied += 1
                        if occupied == 5:
                            new_grid[row, col] = "L"
                            break
        if grid == new_grid:
            break

        grid = new_grid
        new_grid = deepcopy(grid)
    occupied = 0
    for row in range(grid.num_rows):
        for col in range(grid.num_cols):
            if grid[row, col] == "#":
                occupied += 1
    return occupied


def parse(data):
    grid = pah.Grid.from_string(data)
    return grid
    # return data or yield data


def solve_puzzle(soln, a_or_b):
    puzzle = Puzzle(year=2020, day=11)
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
