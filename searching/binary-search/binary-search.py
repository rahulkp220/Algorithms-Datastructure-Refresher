#!/usr/local/bin/python3
import profile

# Iterative solution for binary search
def binary_search(array, key):
    start, end = 0, len(array)-1

    while start <= end:
        mid = (start + end)//2
        
        if array[mid] < key:
            start = mid +1
        elif array[mid] > key:
            end = mid -1
        else:
            return True
    
    return False

if __name__ == '__main__':
    print(binary_search(range(100000000000000000), 10000000111100000))
    profile.run('binary_search(range(100000000000000000), 10000000111100000)')

# Benchmar
# ❯ python3 binary-search/binary-search.py
# True
#          6 function calls in 0.014 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 :0(exec)
#         1    0.000    0.000    0.000    0.000 :0(len)
#         1    0.014    0.014    0.014    0.014 :0(setprofile)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 binary-search.py:5(binary_search)
#         1    0.000    0.000    0.014    0.014 profile:0(binary_search(range(100000000000000000), 10000000111100000))
#         0    0.000             0.000          profile:0(profiler)
