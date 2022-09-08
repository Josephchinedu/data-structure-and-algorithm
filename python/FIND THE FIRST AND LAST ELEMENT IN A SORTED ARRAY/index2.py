from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2


            if nums[mid] < target:
                left = mid + 1

            else:
                right = mid
                
        if nums[left] != target:

            return [-1, -1]

        first = left
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2 + 1

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        return [first, right]


if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))


# explanation https://western-dill-271.notion.site/FIND-THE-FIRST-AND-LAST-ELEMENT-IN-A-SORTED-ARRAY-c1bb1d2f2ee84e46a46dc6406feb030e
    