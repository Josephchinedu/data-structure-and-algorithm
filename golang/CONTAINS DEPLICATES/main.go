package main
import (
	"fmt"
)

func main() {
	nums := []int{1,2,3,1}

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