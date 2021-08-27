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