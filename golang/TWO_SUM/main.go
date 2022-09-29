package main

import (
	"fmt"
)

func main() {
	nums := []int{15, 4, 7, 11, 2, 15}

	target := 13

	result := twoSum(nums, target)
	fmt.Println(result)
}

func twoSum(nums []int, target int) []int {
	var result []int

	for i := 0; i < len(nums); i++ {

		for j := i + 1; j < len(nums); j++ {
			if nums[i]+nums[j] == target {
				result = append(result, i, j)
			}
		}
	}

	return result
}
