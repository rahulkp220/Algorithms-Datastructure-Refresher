package main

import (
	"fmt"
	"time"
)

func binarysearch(array []int64, key int64) bool {
	start, end := 0, len(array)-1

	for start <= end {
		middle := (start + end) / 2
		if array[middle] < key {
			start = middle + 1
		} else if array[middle] > key {
			end = middle - 1
		} else {
			return true
		}
	}
	return false
}

// Helper function to help generate sequence
func xrange(start int64, stop int64) []int64 {
	arr := make([]int64, stop-start+1)
	for i := range arr {
		arr[i] = start + int64(i)
	}
	return arr
}

func main() {
	start := time.Now()
	fmt.Println(binarysearch(xrange(1, 1000000000), 10000001))
	elapsedtime := time.Since(start)
	fmt.Println("Elapsed time ", elapsedtime)
}

/* Sample Run
❯ go run binary_search.go
true
Elapsed time  7.832376304s
*/
