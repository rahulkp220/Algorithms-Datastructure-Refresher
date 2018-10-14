#!/usr/local/bin/julia

function binary_search(array::Array{Int64, 1}, key::Int64)
    bottom, top = 1, length(array)
    while bottom <= top
        middle = floor(Int64, (top + bottom)/2)
        if array[middle] < key
            bottom = middle + 1
        elseif array[middle] > key
            top = middle - 1
        else
            return true
        end
    end
    return false
end

# Sample run 
# julia> @timev binary_search([1:10000000...], 1000011)
#   1.017336 seconds (10.00 M allocations: 310.125 MiB, 77.09% gc time)
# elapsed time (ns): 1017336317
# gc time (ns):      784260295
# bytes allocated:   325189632
# pool allocs:       9999500
# non-pool GC allocs:9
# malloc() calls:    2
# realloc() calls:   6
# GC pauses:         4
# full collections:  2
# true