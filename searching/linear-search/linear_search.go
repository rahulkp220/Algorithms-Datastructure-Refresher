package main

import (
	"fmt"
	"time"
)

func linearsearch(array []int64, key int64) bool {
	for i := 0; i < len(array); i++ {
		if array[i] == key {
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
	fmt.Println(linearsearch(xrange(1, 1000000000), 10000001))
	elapsedtime := time.Since(start)
	fmt.Println("Elapsed time ", elapsedtime)
}

/* Benchmark
❯ go run linear_search.go
true
Elapsed time  7.062523206s
*/
