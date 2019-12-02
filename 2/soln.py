import sys
import copy

a = sys.stdin

nums_str = a.readlines()[0].strip()

nums = [int(s) for s in nums_str.split(",")]
start_nums = copy.deepcopy(nums)
#================================================================================

nums[1] = 12
nums[2] = 2
i = 0
while True:
    instr = nums[i]
    if instr == 99:
        break
    num1 = nums[nums[i + 1]]
    num2 = nums[nums[i + 2]]
    if instr == 1:
        nums[nums[i + 3]] = num1 + num2
    elif instr == 2:
        nums[nums[i + 3]] = num1 * num2
    i += 4


print(nums[0])

#================================================================================

for idx1 in range(100):
    for idx2 in range(100):
        nums = copy.deepcopy(start_nums)
        nums[1] = idx1
        nums[2] = idx2
        i = 0
        while True:
            instr = nums[i]
            if instr == 99:
                break
            num1 = nums[nums[i + 1]]
            num2 = nums[nums[i + 2]]
            if instr == 1:
                nums[nums[i + 3]] = num1 + num2
            elif instr == 2:
                nums[nums[i + 3]] = num1 * num2
            i += 4
        if nums[0] == 19690720:
            print(100 * idx1 + idx2)
            sys.exit()
