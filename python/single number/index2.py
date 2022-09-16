from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        return 2 * sum(set(nums)) - sum(nums)


if __name__ == '__main__':
    print(Solution().singleNumber([4, 1, 2, 1, 2]))
        