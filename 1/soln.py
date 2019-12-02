import sys
import math

a = sys.stdin

nums_str = a.readlines()

nums = [int(s.strip("\n")) for s in nums_str]

#================================================================================

divd = [num // 3 for num in nums]
subd = [num - 2 for num in divd]
print(sum(subd))

#================================================================================
fuel = 0
for num in nums:
    current = num
    while current != 0:
        current = (current // 3) - 2
        if current < 0:
            current = 0
        fuel += current

print(fuel)





