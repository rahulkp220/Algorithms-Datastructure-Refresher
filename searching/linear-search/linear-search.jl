#!/usr/local/bin/julia

function linear_search(array::Array{Int64,1}, key::Int64)
    for i in array
        if i == key
            return true
    return false
        end
    end
end

# Benchmarks
# julia> @timev linear_search([1:100000000...], 10000000)
#  11.617622 seconds (100.00 M allocations: 3.033 GiB, 54.06% gc time)
# elapsed time (ns): 11617622167
# gc time (ns):      6280118240
# bytes allocated:   3256270960
# pool allocs:       99999500
# non-pool GC allocs:9
# malloc() calls:    2
# realloc() calls:   15
# GC pauses:         6
# full collections:  4
# true                          