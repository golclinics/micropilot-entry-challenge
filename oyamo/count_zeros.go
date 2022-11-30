package main

func CountZeroes(A []int) int {
	var count int
	for _, v := range A {
		if v == 0 {
			count++
		}
	}
	return count
}