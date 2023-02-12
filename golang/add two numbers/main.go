package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	result := dummy
	carry := 0

	for l1 != nil || l2 != nil {
		var x, y int
		if l1 != nil {
			x = l1.Val
			l1 = l1.Next
		} else {
			x = 0
		}

		if l2 != nil {
			y = l2.Val
			l2 = l2.Next
		} else {
			y = 0
		}

		sum := x + y + carry
		carry = sum / 10
		result.Next = &ListNode{Val: sum % 10}
		result = result.Next
	}

	return result.Next
}

func main() {
	l1 := &ListNode{Val: 2, Next: &ListNode{Val: 4, Next: &ListNode{Val: 3}}}
	l2 := &ListNode{Val: 5, Next: &ListNode{Val: 6, Next: &ListNode{Val: 4}}}
	result := addTwoNumbers(l1, l2)

	fmt.Println("result", result)
}
