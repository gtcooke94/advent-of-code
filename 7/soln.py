import sys
import copy
from itertools import permutations
from operator import itemgetter
from collections import deque

#  inp = sys.stdin
inp = open("input.txt")

nums_str = inp.readlines()[0].strip('\n')

nums = [int(s) for s in nums_str.split(",")]
start_nums = copy.deepcopy(nums)

def add(x, y, pos):
    nums[pos] = x + y
    return False, None

def mult(x, y, pos):
    nums[pos] = x * y
    return False, None

def input_(pos, val):
    nums[pos] = val
    return False, None

def output_(x):
    print("OUTPUT: {}".format(x))
    return False, x

def jump_true(true, value):
    if true:
        return True, value
    return False, None

def jump_false(true, value):
    if not true:
        return True, value
    return False, None

def lt(a, b, pos):
    if a < b:
        nums[pos] = 1
    else:
        nums[pos] = 0
    return False, None

def eq(a, b, pos):
    if a == b:
        nums[pos] = 1
    else:
        nums[pos] = 0
    return False, None

def end():
    sys.exit()

instructions = {
    1: add,
    2: mult,
    3: input_,
    4: output_,
    5: jump_true,
    6: jump_false,
    7: lt,
    8: eq,
    99: end,
}


instruction_lengths = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    99: 0,
}

def split_instr(instr):
    if instr == 99:
        return instr, []
    if instr < 10:
        instr_str = "0" * instruction_lengths[instr] + "0" + str(instr)
    else:
        instr_str = str(instr)
        digits = [int(i) for i in instr_str]
        l = instruction_lengths[digits[-1]]
        instr_str = "0" * (l + 2 - len(digits)) + instr_str
        instr = int(instr_str[-2:])
        # first param mode to last param mode
    modes = [int(i) for i in instr_str[-3::-1]]
    return instr, modes

       

def run_intcode(nums, inputs):
    i = 0
    to_return = 0
    while True:
        #  print(nums)
        instr = nums[i]
        instr, modes = split_instr(instr)
        if instr == 99:
            break
        l = instruction_lengths[instr]
        params = nums[i+1:i+l+1]
        func_inputs = []
        for j, (p, m) in enumerate(zip(params, modes)):
            # the last instruction
            if j == (l - 1):
                if instr not in (4, 5, 6):
                    # This is a position to place in
                    assert m == 0
                    func_inputs.append(p)
                    continue

            if m == 0:
                func_inputs.append(nums[p])
            elif m == 1:
                func_inputs.append(p)
        if instr == 3:
            func_inputs.append(next(inputs))
        #  print(instr, func_inputs)
        change_ptr, change_to = instructions[instr](*func_inputs)
        if instr == 4:
            to_return = change_to
        if change_ptr:
            i = change_to
        else:
            i += l + 1
    return to_return


#  run_intcode(nums, iter((5,)))
perms = permutations(range(0, 5))
phases_to_val = {}
for phases in perms:
    prev_out = 0
    for phase in phases:
        nums = copy.deepcopy(start_nums)
        prev_out = run_intcode(nums, iter((phase, prev_out)))
    phases_to_val[phases] = prev_out

print(max(phases_to_val.items(), key=itemgetter(1)))

    
#================================================================================















