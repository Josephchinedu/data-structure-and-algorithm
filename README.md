# data-structure-and-algorithm

Big O
##### find the sum of element in array
```bash
num = [1,2,3,4]
n = len(num)
sum = 0

for i in range(0,n):
    sum += num[i]

print("sum of array: ", sum)



############# considering time and space, we've this

num = [1,2,3,4]
n = len(num)
print("sum of array: ", n*(n+1)/2)
```


<hr> </hr>
Binary Search

```bash

import math

def binarysearch(arr,target):
    left = 0
    right = len(arr) - 1

    while(left <= right):
        mid = math.floor(left + (right - left) / 2)

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid+1
        else:
            right = mid - 1

    return -1


arr = [1,2,3,4,5,6]
target = 6

result = binarysearch(arr,target)

if result != -1:
    print("element is present at index %d"%result)
else:
    print("element is not present in array")

```


<hr> </hr>
Linked List

Singly Linked List

```python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        linked_list = ""
        while(temp):
            linked_list += (str(temp.data) + " ")
            temp = temp.next
        print(linked_list)

# Node strucutre: 5 => 1 => 3 => 7


linked_list = LinkedList()
linked_list.head = Node(5)

second_node = Node(1)
third_node = Node(3)
fourth_node = Node(7)

linked_list.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node

linked_list.printList()

```