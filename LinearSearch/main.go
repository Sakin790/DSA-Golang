package main

import "fmt"

func main() {

	arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	value := 11
	for i := 0; i < len(arr); i++ {
		if arr[i] == value {
			fmt.Printf("The value %d was found at index %d\n", value, i)
			break
		}
		if i == len(arr)-1 {
			fmt.Printf("The value %d was not found in the array\n", value)
		}

	}
}
