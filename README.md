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


```python

from typing import List
def rotate_array(nums: List[int], k: int):
    k = k % len(nums)

    ## reverse the entire array
    l, r = 0, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    
    ## reverse the k element
    l, r = 0, k - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
    ## revser the remaining portion of the array

    l, r = k, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1


    print(nums)

rotate_array([1,2,3,4,5,6,7], 3)

## explanation https://gist.github.com/Josephchinedu/371df7559dd5f36d7987bfa919f88359

```


Move zeroes
```python
from typing import List
def move_zeroes(nums: List[int]):
    j = 0
    n = len(nums)
    
    for num in nums:
        if num != 0:
            nums[j] = num
            j += 1
            
    for x in range(j, n):
        nums[x] = 0

## explanation https://gist.github.com/Josephchinedu/2a87c62d4b872355ac7de475ca95bb6d
```


Boats to Save People
```python
from typing import List


def boat_rescue(people: List[int], limit: int) -> int:
    people.sort()
    left = 0
    right = len(people) - 1
    number_of_boats = 0

    while left <= right:
        if left == right:
            number_of_boats += 1
            break
        
        if (people[left] + people[right] <= limit):
            left += 1

        right -= 1
        number_of_boats += 1
    
    return number_of_boats



print(boat_rescue(([3,2,2,1]), 3))

## explanation https://gist.github.com/Josephchinedu/ff508d406513aaddb1480a5e5cbb1d42

```

