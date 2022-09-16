from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums), 2):
            if i == len(nums) - 1 or nums[i] != nums[i + 1]:
                return nums[i]


if __name__ == '__main__':
    print(Solution().singleNumber([4, 1, 2, 1, 2]))