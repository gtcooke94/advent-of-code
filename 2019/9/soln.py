import sys
import copy

#  inp = sys.stdin
inp = open("input.txt")

nums_str = inp.readlines()[0].strip('\n')

#  import pdb; pdb.set_trace()
nums = [int(s) for s in nums_str.split(",")]
nums.extend([0] * len(nums) ** 2)
start_nums = copy.deepcopy(nums)

global i
global relative_base
relative_base = 0

def add(x, y, pos):
    nums[pos] = x + y
    return True

def mult(x, y, pos):
    nums[pos] = x * y
    return True

def input_(pos):
    nums[pos] = 2
    return True

def output_(x):
    print("OUTPUT: {}".format(x))
    return True

def jump_true(true, value):
    global i
    if true:
        i = value
        return False
    return True

def jump_false(true, value):
    global i
    if not true:
        i = value
        return False
    return True

def lt(a, b, pos):
    if a < b:
        nums[pos] = 1
    else:
        nums[pos] = 0
    return True

def eq(a, b, pos):
    if a == b:
        nums[pos] = 1
    else:
        nums[pos] = 0
    return True

def change_base(value):
    global relative_base
    relative_base += value
    return True

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
    9: change_base,
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
    9: 1,
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

       


#================================================================================

#  import pdb; pdb.set_trace()
#  nums[1] = 12
#  nums[2] = 2
i = 0
#  import pdb; pdb.set_trace()
while True:
    #  print(nums)
    instr = nums[i]
    instr, modes = split_instr(instr)
    if instr == 3 and modes == [2]:
        pass
        #  import pdb; pdb.set_trace()
    if instr == 99:
        break
    l = instruction_lengths[instr]
    params = nums[i+1:i+l+1]
    func_inputs = []
    #  import pdb; pdb.set_trace()
    for j, (p, m) in enumerate(zip(params, modes)):
        # the last instruction
        if j == (l - 1):
            if instr in (0, 1, 2, 3, 7, 8):
                # This is a position to place in
                assert m == 0 or m == 2
                if m == 0:
                    func_inputs.append(p)
                elif m == 2:
                    func_inputs.append(p + relative_base)
                continue

        if m == 0:
            func_inputs.append(nums[p])
        elif m == 1:
            func_inputs.append(p)
        elif m == 2:
            func_inputs.append(nums[p + relative_base])
    #  print(instr, func_inputs)
    change_ptr = instructions[instr](*func_inputs)
    if change_ptr:
        i += l + 1



