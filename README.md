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
