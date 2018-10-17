#!/usr/local/bin/julia

function bubbleSort(array::Array{Int64, 1})
    array_length = length(array)
    for iteration in 1:array_length
        for item in 1:array_length-iteration-1
            if array[item] > array[item+1]
                array[item], array[item+1] = array[item+1], array[item]
            end
        end
    end
    return array
end 

# julia> a = [12,24,48,11,23,45,9,7,5,78]
# julia> bubbleSort(a)
# 10-element Array{Int64,1}:
#   5
#   7
#   9
#  11
#  12
#  23
#  24
#  45
#  48
#  78