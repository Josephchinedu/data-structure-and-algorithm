from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        index = 1
        while index < len(arr) and arr[index] > arr[index - 1]:
            index += 1
            
        if index == 1 or index == len(arr):
            return False
        
        while index < len(arr) and arr[index] < arr[index - 1]:
            index += 1
            
        return index == len(arr)

## explanation https://gist.github.com/Josephchinedu/bc33a495f05a191270ce928c4847c599