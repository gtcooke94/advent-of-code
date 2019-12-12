import sys
import copy
from itertools import permutations
from operator import itemgetter
from collections import deque
from itertools import cycle

#  inp = sys.stdin
inp = open("5in.txt")

nums_str = inp.readlines()[0].strip('\n')

nums = [int(s) for s in nums_str.split(",")]
start_nums = copy.deepcopy(nums)

def add(x, y, pos, nums):
    nums[pos] = x + y
    return False, None

def mult(x, y, pos, nums):
    nums[pos] = x * y
    return False, None

def input_(pos, val, nums):
    nums[pos] = val
    return False, None

def output_(x, nums):
    #  if x == 3856051:
        #  import pdb; pdb.set_trace()
    print("OUTPUT: {}".format(x))
    return False, x

def jump_true(true, value, nums):
    if true:
        return True, value
    return False, None

def jump_false(true, value, nums):
    if not true:
        return True, value
    return False, None

def lt(a, b, pos, nums):
    if a < b:
        nums[pos] = 1
    else:
        nums[pos] = 0
    return False, None

def eq(a, b, pos, nums):
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

       
def init_intcode(nums, inputs):
    return run_intcode(nums, inputs, 0)

def run_intcode(nums, inputs, i):
    to_return = 0
    is_done = False
    is_waiting_for_input = False
    my_output = None
    while True:
        #  print(nums)
        instr = nums[i]
        instr, modes = split_instr(instr)
        #  print(instr)
        #  import pdb; pdb.set_trace()
        if instr == 99:
            is_done = True
            io.append(my_output)
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
            try:
                func_inputs.append(next(inputs))
            except StopIteration:
                try:
                    func_inputs.append(io.popleft())
                except IndexError:
                    io.append(my_output)
                    is_waiting_for_input = True
                    break
        #  print(instr, func_inputs)
        func_inputs.append(nums)
        change_ptr, instr_out = instructions[instr](*func_inputs)
        if change_ptr:
            i = instr_out
        else:
            i += l + 1
        if instr == 4:
            #  to_return = instr_out
            my_output = instr_out
            #  io.append(instr_out)
    return to_return, i, is_waiting_for_input, is_done


#  run_intcode(nums, iter((5,)))
#  perms = permutations(range(0, 5))
#  phases_to_val = {}
#  for phases in perms:
#      prev_out = 0
#      for phase in phases:
#          nums = copy.deepcopy(start_nums)
#          prev_out = run_intcode(nums, iter((phase, prev_out)))
#      phases_to_val[phases] = prev_out
#
#  print(max(phases_to_val.items(), key=itemgetter(1)))

    
#================================================================================

perms = permutations(range(5, 10))
phases_to_val = {}


def handle_pause(cur_iter, to_return, instr_ptr, is_waiting_for_input, is_done):
    pointers[cur_iter] = instr_ptr
    all_done[cur_iter] = is_done
    return is_done, all(all_done)



phases_to_val = {}
for phases in perms:
    memories = [
        copy.deepcopy(start_nums),
        copy.deepcopy(start_nums),
        copy.deepcopy(start_nums),
        copy.deepcopy(start_nums),
        copy.deepcopy(start_nums),
    ]

    pointers = [0] * 5
    all_done = [False] * 5
    io = deque()
    io.append(0)
    phases = list(phases)
    done = False
    for cur_iter in range(5):
        #  import pdb; pdb.set_trace()
        this_done, full_done = handle_pause(cur_iter, *init_intcode(memories[cur_iter], iter((phases[cur_iter],))))
        
    if not full_done:
        for cur_iter in cycle(range(5)):
            #  import pdb; pdb.set_trace()
            this_done, full_done = handle_pause(cur_iter, *run_intcode(memories[cur_iter], iter(()), pointers[cur_iter]))
            if full_done:
                break
    assert len(io) == 1
    val = io.popleft()
    print(val)
    phases_to_val[tuple(phases)] = val

print(max(phases_to_val.items(), key=itemgetter(1)))
