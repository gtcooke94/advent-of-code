MASK = "mask"
ASSIGN = "assign"

class DockingMemory:
    MEM_LENGTH = 36

    def __init__(self):
        self.mask = None
        self.mem = {}

    def do_operation(self, op):
        if type(op) is MaskOperation:
            self.mask = op.mask
        elif type(op) is AssignOperation:
            self._update_memory(op.location, op.value)
        
    def _update_memory(self, loc, value):
        value = self._mask_value(value)
        self.mem[loc] = int(value, 2)

    def _mask_value(self, value):
        value = bin(value)[2:]
        if len(value) < self.MEM_LENGTH:
            value = f"{''.join('0' for _ in range(self.MEM_LENGTH - len(value)))}{value}"
            value = list(value)
        for i in range(self.MEM_LENGTH):
            if self.mask[i] == "X":
                continue
            value[i] = self.mask[i]
        return "".join(value)

    def sum_memory(self):
        return sum(self.mem.values())

class DockingMemory2:
    MEM_LENGTH = 36

    def __init__(self):
        self.mask = None
        self.mem = {}

    def do_operation(self, op):
        if type(op) is MaskOperation:
            self.mask = op.mask
        elif type(op) is AssignOperation:
            self._update_memory(op.location, op.value)
        
    def _update_memory(self, loc, value):
        locs = self._mask_location(loc)
        for loc in locs:
            self.mem[int(loc, 2)] = value

    def _mask_location(self, loc):
        loc = bin(loc)[2:]
        if len(loc) < self.MEM_LENGTH:
            loc = f"{''.join('0' for _ in range(self.MEM_LENGTH - len(loc)))}{loc}"
            loc = list(loc)
        for i in range(self.MEM_LENGTH):
            if self.mask[i] == "X":
                loc[i]  = "X"
            elif self.mask[i] == "0":
                continue
            elif self.mask[i] == "1":
                loc[i] = "1"
        if "X" not in loc:
            yield "".join(loc)
            return
        locs = []
        locs.append("".join(loc))
        for i in range(self.MEM_LENGTH):
            if loc[i] == "X":
                new_locs = []
                for floating_loc in locs:
                    fuzzy = list(floating_loc)
                    fuzzy[i] = "0"
                    new_locs.append("".join(fuzzy))
                    fuzzy[i] = "1"
                    new_locs.append("".join(fuzzy))
                locs = new_locs
        yield from new_locs 

    def sum_memory(self):
        return sum(self.mem.values())
        
class MaskOperation():
    def __init__(self, content):
        self.opType = MASK
        self.mask = content.strip(" ")
    
    def __repr__(self):
        return f"MaskOperation(opType={self.opType}, mask={self.mask})"

class AssignOperation():
    def __init__(self, content):
        self.opType = ASSIGN
        self.location = int(content.split("[")[1].split("]")[0])
        self.value = int((content.split("=")[1].strip()))
    
    def __repr__(self):
        return f"AssignOperation(opType={self.opType}, location={self.location}, value={self.value})"