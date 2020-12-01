import sys
from operator import itemgetter
import math

inp = open("input.txt")

lines = inp.readlines()
lines = [line.strip("\n") for line in lines]


rows = len(lines)
cols = len(lines[0])
asteroids = {}
for row, line in enumerate(lines):
    for col, val in enumerate(line):
        if val == "#":
            asteroids[(row, col)] = 0


def get_line(base_r, base_c, r, c):
    if base_r - r == 0:
        return lambda x: x == base_r
    slope = (base_c - c) / (base_r - r)
    b = base_c - slope * base_r
    line = lambda x: slope * x + b
    return line

def horizontal_check(row, col, r, c):
    is_blocked = False
    if col <= c:
        this_cols = list(range(col + 1, c))
    else:
        this_cols = list(range(c + 1, col))
    for this_col in this_cols:
        if (row, this_col) in asteroids.keys():
            is_blocked = True
            break
    return is_blocked

def tup_compare(a, b):
    is_equal = True
    for (aa, bb) in zip(a, b):
        is_equal &= math.isclose(aa, bb)
    return is_equal

 



def check_los(row, col, r, c):
    #  import pdb; pdb.set_trace()
    #  print(row, col, r, c)
    #  import pdb; pdb.set_trace()
    if row - r == 0:
        return horizontal_check(row, col, r, c)
    line = get_line(row, col, r, c)
    if row <= r:
        this_rows = list(range(row, r + 1))
    else:
        this_rows = list(range(r, row + 1))
    #  if col <= c:
    #      this_cols = list(range(col, c + 1))
    #  else:
    #      this_cols = list(range(c, col + 1))

    is_blocked = False
    for this_row in this_rows:
        this_col = line(this_row)
        #  if (this_row, this_col) == (r, c) or (this_row, this_col) == (row, col):
        if tup_compare((this_row, this_col), (r, c)) or tup_compare((this_row, this_col), (row, col)):
            continue
        #  print(this_row, this_col)
        for key in asteroids.keys():
            if tup_compare((this_row, this_col), key):
                is_blocked = True
                return is_blocked
        #  if (this_row, this_col) in asteroids.keys():
        #      is_blocked = True
        #      return True
    #  for this_row in this_rows:
    #      if blocked:
    #          break
    #      for this_col in this_cols:
    #          if (this_row, this_col) == (r, c) or (this_row, this_col) == (row, col):
    #              continue
    #          if line(this_row) == this_col:
    #              if (this_row, this_col) in  asteroids.keys():
    #                  blocked = True
    #                  break
    return is_blocked


#  for (row, col) in asteroids.keys():
#      #  if (row, col) == (0, 1):
#      #      import pdb; pdb.set_trace()
#      for r in range(rows):
#          for c in range(cols):
#              #  if (r, c) == (4, 3):
#              #      import pdb; pdb.set_trace()
#              if r == row and c == col:
#                  continue
#              if (r, c) not in asteroids.keys():
#                  continue
#              blocked = check_los(row, col, r, c)
#              asteroids[(row, col)] += not bl

#  ================================================================================
# Part 2 
# This is also a much better solution that part1. Just calc the angles_asteroids dict for each asteroid, then the answer to part 1 is the length of that dictionary.
center = (11, 19)
center_row, center_col = center
def calc_angle(row, col):
    rad = math.atan2(center_row-row, col-center_col)
    if rad >= 0:
        if rad <= math.pi / 2:
            rad = math.pi / 2 - rad
        else:
            rad = 2 * math.pi - rad + math.pi/2
    elif rad < 0:
        rad = -rad + math.pi/2

    return rad

from collections import defaultdict, deque
from itertools import cycle
angles_asteroids = defaultdict(deque)
for r, c in asteroids.keys():
    if (r, c) == center:
        continue
    angle = calc_angle(r, c)
    angles_asteroids[angle].append((r, c))

sorted_angles = sorted(angles_asteroids.keys())
counter = 0
for angle in cycle(sorted_angles):
    try:
        a = angles_asteroids[angle].popleft()
        counter += 1
        if counter == 200:
            break
    except Exception:
        continue 

print(a[1] * 100 + a[0])
         

