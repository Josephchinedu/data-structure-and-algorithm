package main

import "fmt"

func isPalindrome(s string) bool {
	left := 0
	right := len(s) - 1

	for left < right {
		if s[left] != s[right] {
			return false
		}

		left++
		right--
	}

	return true
}

func main() {
	s := "racecar"
	result := isPalindrome(s)
	fmt.Println(result)
}
