import time
from soln import solve
from better_solve import better_solve
from memory_profiler import profile

# Better solve uses less memory, but takes slightly longer
# Could merge the two and not use the object overhead and only store lists with 2 items, but it would be unnecessary and messy
""" Results
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     7     36.8 MiB     36.8 MiB           1   @profile
     8                                         def main():
     9     36.8 MiB      0.0 MiB           1       inp = [2, 0, 1, 9, 5, 19]
    10     36.8 MiB      0.0 MiB           1       final_pos = 30000000
    11     36.8 MiB      0.0 MiB           1       tic = time.time()
    12     40.9 MiB      4.1 MiB           1       solve(inp, final_pos)
    13     40.9 MiB      0.0 MiB           1       toc = time.time()
    14     40.9 MiB      0.0 MiB           1       print(f"Base solution: {toc - tic} seconds")
    15     40.9 MiB      0.0 MiB           1       tic = time.time()
    16     41.7 MiB      0.9 MiB           1       better_solve(inp, final_pos)
    17     41.7 MiB      0.0 MiB           1       toc = time.time()
    18     41.7 MiB      0.0 MiB           1       print(f"Better solution: {toc - tic} seconds")

-------------------------------------------------------------
Base solution: 24.498153686523438 seconds
Better solution: 28.303056240081787 seconds
"""

@profile
def main():
    inp = [2, 0, 1, 9, 5, 19]
    final_pos = 30000000
    tic = time.time()
    solve(inp, final_pos)
    toc = time.time()
    print(f"Base solution: {toc - tic} seconds")
    tic = time.time()
    better_solve(inp, final_pos)
    toc = time.time()
    print(f"Better solution: {toc - tic} seconds")

if __name__ == "__main__":
    main()
