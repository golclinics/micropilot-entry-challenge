package main

import "fmt"

func CountZeros(A []int) int {
	var count int
	for _, v := range A {
		if v == 0 {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(CountZeros([]int{1, 0, 5, 6, 0, 2}))
}
