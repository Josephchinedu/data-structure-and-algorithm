from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, n in enumerate(nums):
            
            if n != i:
                return i
        return len(nums) 

if __name__ == '__main__':
    nums = [9,6,4,2,3,5,7,0,1]
    print(Solution().missingNumber(nums))