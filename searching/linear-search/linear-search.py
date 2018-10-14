# Uses Python3

import profile
def linear_search(array, key):
    for i in array:
        if i == key:
            return True
    return False

if __name__ == "__main__":
    profile.run('linear_search(range(100000000000), 100000001)')
    
## Benchmark
"""
❯ python3 linear-search.py
         5 function calls in 7.213 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    7.188    7.188 :0(exec)
        1    0.024    0.024    0.024    0.024 :0(setprofile)
        1    0.000    0.000    7.188    7.188 <string>:1(<module>)
        1    7.188    7.188    7.188    7.188 linear-search.py:4(linear_search)
        1    0.000    0.000    7.213    7.213 profile:0(linear_search(range(1000000000), 100000001))
        0    0.000             0.000          profile:0(profiler)
"""