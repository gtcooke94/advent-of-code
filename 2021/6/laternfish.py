from collections import Counter
import copy

class LanternFish:
    def __init__(self, timer):
        self.timer = timer

    def step(self):
        self.timer -= 1
        if self.timer == 0:
            self.timer = 7
            return LanternFish(9)


        

def counter_solution(starting_timer, days):
    fish_counter_by_timer = Counter()
    for t in starting_timer:
        fish_counter_by_timer[t] += 1
    for d in range(days):
        new_counter = Counter()
        for k, v in fish_counter_by_timer.items():
            if k == 0:
                new_counter[8] += v
                new_counter[6] += v
            else:
                new_counter[k - 1] += v
        fish_counter_by_timer = new_counter
    return sum(fish_counter_by_timer.values())
    





    