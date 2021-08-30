package main

import (
	"fmt"
)

func CountZeros(A []int) {

	count := 0
	for index := 0; index < len(A); index++ {

		if A[index] == 0 {

			count = count + 1
		}
	}
	fmt.Println(count)
}

func main() {
	array := []int{1, 0, 5, 6, 0, 2} //2
	CountZeros(array)

}
