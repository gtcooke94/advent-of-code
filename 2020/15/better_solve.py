from collections import Counter, defaultdict

def better_solve(nums, final_position):
    memory = defaultdict(PositionStorage)
    for i, num in enumerate(nums):
        memory[num].update(i + 1)

    pos = len(nums) + 1
    # In my puzzle input, starting numbers aren't repeated, so after that we get a 0
    last_number = nums[-1]
    while pos <= final_position:
        current_number = 0
        if memory[last_number].spoken_multiple():
            current_number = memory[last_number].difference()
        memory[current_number].update(pos)
        last_number = current_number
        pos += 1
        
    return last_number

class PositionStorage:
    most_recent = None
    second_most_recent = None

    def update(self, i):
        if self.most_recent is None:
            self.most_recent = i
        else:
            self.second_most_recent = self.most_recent
            self.most_recent = i
        
    def spoken_multiple(self):
        return self.most_recent is not None and self.second_most_recent is not None

    def difference(self):
        return self.most_recent - self.second_most_recent