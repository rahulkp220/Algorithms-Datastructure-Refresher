package main

import (
	"fmt"
)

func bubbleSort(array []int) []int {
	arrayLength := len(array)

	for i := 0; i < arrayLength; i++ {
		for j := 0; j < arrayLength-i-1; j++ {

			if array[j] > array[j+1] {
				array[j], array[j+1] = array[j+1], array[j]
			}
		}
	}
	return array
}

func main() {
	a := []int{12, 24, 48, 11, 23, 45, 9, 7, 5, 78}
	fmt.Println(bubbleSort(a))
}

// Output
// $ go run bubble_sort.go
// [5 7 9 11 12 23 24 45 48 78]
