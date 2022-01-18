import numpy as np
from collections import Counter

base_mat = np.matrix([
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
], dtype="int64")

def matrix_solve(initial_timers, days):
    initial_timers = Counter(initial_timers)
    initial_timers_vec = [0 for _ in range(9)]
    for i in range(0, 9):
        initial_timers_vec[i] = initial_timers[i]
    solution_mat = np.linalg.matrix_power(base_mat, days)
    initial_timers = np.array(initial_timers_vec)
    return np.sum(np.matmul(solution_mat, initial_timers))
