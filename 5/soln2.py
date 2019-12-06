import sys
import copy

#  inp = sys.stdin
inp = open("input.txt")

nums_str = inp.readlines()[0].strip()

nums = [int(s) for s in nums_str.split(",")]
start_nums = copy.deepcopy(nums)


def add(x, y, pos):
    nums[pos] = x + y
    return True

def mult(x, y, pos):
    nums[pos] = x * y
    return True

def input_(pos):
    nums[pos] = 1
    return True

def output_(x):
    print("OUTPUT: {}".format(x))
    return True

def jump(yes, value):


def end():
    sys.exit()

instructions = {
    1: add,
    2: mult,
    3: input_,
    4: output_,
    99: end,
}


instruction_lengths = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 0,
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

#  nums[1] = 12
#  nums[2] = 2
global i
i = 0
while True:
    #  import pdb; pdb.set_trace()
    instr = nums[i]
    instr, modes = split_instr(instr)
    if instr == 99:
        break
    l = instruction_lengths[instr]
    params = nums[i+1:i+l+1]
    func_inputs = []
    #  import pdb; pdb.set_trace()
    for j, (p, m) in enumerate(zip(params, modes)):
        # the last instruction
        if j == (l - 1):
            if instr != 4:
                # This is a position to place in
                assert m == 0
                func_inputs.append(p)
                continue

        if m == 0:
            func_inputs.append(nums[p])
        elif m == 1:
            func_inputs.append(p)
    change_ptr = instructions[instr](*func_inputs)
    if change_ptr:
        i += l + 1

#  print(nums)


#================================================================================
#
#  for idx1 in range(100):
#      for idx2 in range(100):
#          nums = copy.deepcopy(start_nums)
#          nums[1] = idx1
#          nums[2] = idx2
#          i = 0
#          while True:
#              instr = nums[i]
#              if instr == 99:
#                  break
#              num1 = nums[nums[i + 1]]
#              num2 = nums[nums[i + 2]]
#              if instr == 1:
#                  nums[nums[i + 3]] = num1 + num2
#              elif instr == 2:
#                  nums[nums[i + 3]] = num1 * num2
#              i += 4
#          if nums[0] == 19690720:
#              print(100 * idx1 + idx2)
#              sys.exit()
