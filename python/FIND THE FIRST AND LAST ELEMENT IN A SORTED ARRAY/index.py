from typing import List


class Solution:

    def getLeftPosition(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                if mid - 1 >= 0 and nums[mid - 1] != target or mid == 0:
                    return mid

                right = mid - 1

            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def getRightPosition(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                if mid + 1 < len(nums) and nums[mid + 1] != target or mid == len(nums) - 1:
                    return mid

                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1



    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = self.getLeftPosition(nums, target)
        right = self.getRightPosition(nums, target)

        return [left, right]


if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))


# explanation https://western-dill-271.notion.site/FIND-THE-FIRST-AND-LAST-ELEMENT-IN-A-SORTED-ARRAY-c1bb1d2f2ee84e46a46dc6406feb030e