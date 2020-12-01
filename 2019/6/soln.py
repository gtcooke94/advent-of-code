import sys
import math
from collections import defaultdict
from collections import deque

inp = open("input.txt")

lines = inp.readlines()

to_from = []
all_orbits = set()

for line in lines:
    to, f = line.strip("\n").split(")")
    to_from.append([to, f])
    all_orbits.update([to, f])

#  to_from = {to: f for line in lines for to, f in line.strip("\n").split(")")}

orbit_dicts = {o: [] for o in all_orbits}

for connection in to_from:
    to, f = connection
    orbit_dicts[to].append({f: orbit_dicts[f]})
    #  print(to, f)
    #  print(orbit_dicts)


def add_as_center(o):
    if not orbit_dicts[o]:
        return 0
    running_sum = 0
    orbits_list = orbit_dicts[o]
    for suborbits_dict in orbit_dicts[o]:
        for subo in suborbits_dict.keys():
            running_sum = 1 + running_sum + add_as_center(subo)
    return running_sum

checksum = 0
for o in all_orbits:
    checksum += add_as_center(o)
        

print(checksum)

#  ================================================================================
flatlist = defaultdict(list)
for o in all_orbits:
    orbits_list = orbit_dicts[o]
    direct = [list(a.keys())[0] for a in orbits_list]
    flatlist[o].extend(direct)
    for d in direct:
        flatlist[d].append(o)
    

def bfs(root, target):
    q = deque([(root, 0)])
    visited = set()
    while q:
        cur, d = q.popleft()
        if cur in visited:
            continue
        visited.update([cur])
        to_add = flatlist[cur]
        if "SAN" in to_add:
            print(d-1)
            break
        for node in to_add:
            q.append((node, d + 1))


bfs("YOU", "SAN")

        




        




        






    # ================================================================================
