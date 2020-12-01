global i

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

while True:
    #  print(nums)
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
            if instr not in (4, 5, 6):
                # This is a position to place in
                assert m == 0
                func_inputs.append(p)
                continue

        if m == 0:
            func_inputs.append(nums[p])
        elif m == 1:
            func_inputs.append(p)
    #  print(instr, func_inputs)
    change_ptr = instructions[instr](*func_inputs)
    if change_ptr:
        i += l + 1
