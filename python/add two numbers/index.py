# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        # print(self.val)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode()
        current = head
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            current.next = ListNode(carry % 10)
            current = current.next
            carry = carry // 10
        return head.next


# Time Complexity: O(max(m,n))
# Space Complexity: O(max(m,n))

# Runtime: 68 ms, faster than 94.18% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14.3 MB, less than 43.75% of Python3 online submissions for Add Two Numbers.

# example 1
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]

if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = Solution().addTwoNumbers(l1, l2)
    print(result.val, result.next.val, result.next.next.val)
