package main

import "fmt"

func main() {
	arr := []int{64, 25, 12, 22, 11}
	fmt.Println("Original array:", arr)

	SelectionSort(arr)
	fmt.Println("Sorted array:", arr)
}

func BubbleSort() {
	arr := []int{1, 8, 3, 1, 4}
	rangeValue := len(arr)
	for i := 0; i < rangeValue; i++ {
		for j := 0; j < rangeValue-i-1; j++ {
			//{1, 8, 3, 1, 4}
			//1,3,1,4,8
			//1,1,3,4,8
			if arr[j] > arr[j+1] {
				// swap
				temp := arr[j]
				arr[j] = arr[j+1] //
				arr[j+1] = temp
			}
		}
	}

	fmt.Println(arr)
}

func SelectionSort(arr []int) {
	n := len(arr)
	for i := 0; i < n-1; i++ {
		// Assume the minimum is the first element
		minIndex := i
		// Find the minimum element in unsorted portion

		
		//arr := []int{64, 25, 12, 22, 11}
		for j := i + 1; j < n; j++ {
			if arr[j] < arr[minIndex] {
				minIndex = j
			}
		}

		// Swap the found minimum element with the first element of the unsorted portion
		if minIndex != i {
			arr[i], arr[minIndex] = arr[minIndex], arr[i]
		}
	}
}
