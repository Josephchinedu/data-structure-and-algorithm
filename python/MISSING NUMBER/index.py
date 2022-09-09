from typing import List


class Solution:

    def sort_array(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        pivot = nums[0]
        left = [i for i in nums[1:] if i <= pivot]
        right = [i for i in nums[1:] if i > pivot]
        return self.sort_array(left) + [pivot] + self.sort_array(right)

    def _number_diff(self, a, b):
        return a - b

    def missingNumber(self, nums: List[int]) -> int:
        sorted_array = self.sort_array(nums)
        
        previous_element = sorted_array[0]

        for element in sorted_array[1:]:
            if self._number_diff(element, previous_element) > 1:

                return element - 1

            previous_element = element


if __name__ == '__main__':
    nums = [9,6,4,2,3,5,7,0,1]
    
    print(Solution().missingNumber(nums))