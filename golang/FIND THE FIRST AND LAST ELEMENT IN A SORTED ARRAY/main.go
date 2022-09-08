package main

import "fmt"

func main() {
	var nums = []int{5, 7, 7, 8, 8, 10}
	var target = 8
	var result = searchRange(nums, target)
	fmt.Println(result)
}

func searchRange(nums []int, target int) []int {
	var result = []int{-1, -1}

	var left = 0
	var right = len(nums) - 1
	var mid = 0

	for left <= right {

		mid = left + (right-left)/2

		fmt.Println("mid", mid)

		if nums[mid] == target {

			var i = mid

			for i >= 0 && nums[i] == target {
				i--

			}
			result[0] = i + 1

			i = mid

			for i < len(nums) && nums[i] == target {
				i++
			}

			result[1] = i - 1

			return result

		} else if nums[mid] > target {

			right = mid - 1

		} else {

			left = mid + 1

		}
	}

	return result
}

// explanation https://western-dill-271.notion.site/FIND-THE-FIRST-AND-LAST-ELEMENT-IN-A-SORTED-ARRAY-c1bb1d2f2ee84e46a46dc6406feb030e
