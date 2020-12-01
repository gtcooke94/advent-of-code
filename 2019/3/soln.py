import sys
import math
import numpy as np
np.set_printoptions(edgeitems=30, linewidth=100000)

a = sys.stdin

nums_str = a.readlines()

twopaths = [s.strip("\n") for s in nums_str]

path1 = twopaths[0].split(",")
path2 = twopaths[1].split(",")

path1dir = [s[0] for s in path1]
path1distance = [int(s[1:]) for s in path1]
path2dir = [s[0] for s in path2]
path2distance = [int(s[1:]) for s in path2]

print(path1dir)
print(path1distance)
print(path2dir)
print(path2distance)



gridsize = 50000 
midpoint = gridsize // 2
#================================================================================
#  grid1 = np.zeros((gridsize, gridsize))
#  grid2= np.zeros((gridsize, gridsize))

def draw(direction, dis, x1, x2, marker):
    if marker == 1:
        grid = grid1
    else:
        grid = grid2

    if direction == 'U':
        grid[x1-dis:x1+1, x2] = marker
        x1 = x1-dis
    if direction == 'R':
        grid[x1, x2:x2+dis+1] = marker
        x2 = x2+dis
    if direction == 'D':
        grid[x1:x1+dis+1, x2] = marker
        x1 = x1+dis
    if direction == 'L':
        grid[x1, x2-dis:x2+1] = marker
        x2 = x2-dis
    return x1, x2

#  x1 = midpoint
#  x2 = midpoint
#  for direction, dis in zip(path1dir, path1distance):
#      x1, x2 = draw(direction, dis, x1, x2, 1)
#
#  x1 = midpoint
#  x2 = midpoint
#  for direction, dis in zip(path2dir, path2distance):
#      x1, x2 = draw(direction, dis, x1, x2, 2)
#
#  grid = grid1 + grid2
#
#  intx, inty = np.where(grid == 3)
#
#  curmin = np.inf
#  for x, y in zip(intx, inty):
#      dist = np.abs(x - midpoint) + np.abs(y - midpoint)
#      if dist == 0:
#          continue
#      print(dist)
#      if dist < curmin:
#          curmin = dist
#
#  print(intx, inty)
#  print(curmin)
#  print(grid)


#================================================================================
def draw2(direction, dis, x1, x2, marker, counter):
    new_counter = counter+dis
    total_length_addition = np.array(range(counter, new_counter+1))
    if marker == 1:
        grid = grid1
        distgrid = distgrid1
    else:
        grid = grid2
        distgrid = distgrid2
    if direction == 'U' or direction == 'D':
        x1range = None
        if direction == 'U':
            x1range = range(x1, x1-dis-1, -1)
            #  grid[x1-dis:x1+1, x2] = marker
            #  distgrid[x1-dis:x1+1, x2] = total_length_addition
            x1 = x1-dis
        elif direction == 'D':
            x1range = range(x1, x1+dis+1)
            #  grid[x1:x1+dis+1, x2] = marker
            #  distgrid[x1:x1+dis+1, x2] = total_length_addition
            x1 = x1+dis
        for x1cur in x1range:
            grid[x1cur, x2] = marker
            if distgrid[x1cur, x2] == 0:
                distgrid[x1cur, x2] = counter
            counter += 1
    elif direction == 'R' or direction == 'L':
        x2range = None
        if direction == 'R':
            x2range = range(x2, x2+dis+1)
            #  grid[x1, x2:x2+dis+1] = marker
            #  distgrid[x1, x2:x2+dis+1] = total_length_addition
            x2 = x2+dis
        if direction == 'L':
            x2range = range(x2, x2-dis-1, -1)
            #  grid[x1, x2-dis:x2+1] = marker
            #  distgrid[x1, x2-dis:x2+1] = total_length_addition
            x2 = x2-dis
        for x2cur in x2range:
            grid[x1, x2cur] = marker
            if distgrid[x1, x2cur] == 0:
                distgrid[x1, x2cur] = counter
            counter += 1

    return x1, x2, new_counter

grid1 = np.zeros((gridsize, gridsize))
grid2= np.zeros((gridsize, gridsize))
distgrid1 = np.zeros((gridsize, gridsize))
distgrid2= np.zeros((gridsize, gridsize))
x1 = midpoint
x2 = midpoint
counter = 0
for direction, dis in zip(path1dir, path1distance):
    x1, x2, counter = draw2(direction, dis, x1, x2, 1, counter)

x1 = midpoint
x2 = midpoint 
counter = 0 
for direction, dis in zip(path2dir, path2distance):
    x1, x2, counter = draw2(direction, dis, x1, x2, 2, counter)

grid = grid1 + grid2

intx, inty = np.where(grid == 3)

curmin = np.inf
#  print(distgrid1)
#  print(distgrid2)
for x, y in zip(intx, inty):
    traveledG1 = distgrid1[x, y]
    traveledG2 = distgrid2[x, y]
    dist = traveledG1 + traveledG2
    #  print(dist)
    if dist == 0:
        continue
    if dist < curmin:
        curmin = dist

print(intx, inty)
print(curmin)
#  print(grid)





