package main

import (
	"fmt"
)

func main() {
	nums := []int{2, 2, 1, 1, 1, 2, 2}

	result := majorityElement(nums)
	fmt.Println(result)
}

func majorityElement(nums []int) int {
	var count int
	var result int

	for i := 0; i < len(nums); i++ {
		count = 0

		for j := 0; j < len(nums); j++ {
			if nums[i] == nums[j] {
				count++
			}
		}

		if count > len(nums)/2 {
			result = nums[i]
		}
	}

	return result
}
