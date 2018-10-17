#!/usr/bin/local/python3

def bubble_sort(array):
    """
    Bubble Sort in Python3!
    """
    array_length = len(array)

    # iterate over the array
    for iteration in range(array_length):
        # for each iteraion, compare each pair of items in this array
        for item in range(0, array_length-iteration-1):
            # if the item is greater, swap it
            if array[item] > array[item+1]:
                array[item], array[item+1] = array[item+1], array[item]
    
    return array

if __name__ == "__main__":
    array = [12,24,48,11,23,45,9,7,5,78]
    print(bubble_sort(array))