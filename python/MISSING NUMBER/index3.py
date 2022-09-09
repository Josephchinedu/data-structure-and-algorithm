from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        current_sum = sum(nums)
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        return expected_sum - current_sum

if __name__ == '__main__':
    nums = [9,6,4,2,3,5,7,0,1]
    print(Solution().missingNumber(nums))