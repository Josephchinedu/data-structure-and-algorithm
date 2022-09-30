package main
import (
	"fmt"
)

func main() {
	nums := []int{15,11, 4, 7, 11, 2, 15}

	result := containsDuplicates(nums)
	fmt.Println(result)
}

func containsDuplicates(nums []int) bool {
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] == nums[j] {
				return true
			}
		}
	}

	return false
}