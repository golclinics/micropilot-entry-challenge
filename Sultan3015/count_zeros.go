package main

import "fmt"

func CountZeros(A []int) {
	count := 0
	for _, element := range A {
		if element == 0 {
			count = count + 1
		}
	}
	fmt.Println(count)
}
func main() {
	array := []int{1, 0, 5, 6, 0, 2}
	CountZeros(array)

}
