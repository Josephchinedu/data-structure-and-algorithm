class Solution:
    def majority_element(self, nums: list) -> int:
        m = {}
        for i in nums:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        for i in m:
            if m[i] > len(nums)//2:
                return i
        return -1


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    sol = Solution()
    print(sol.majority_element(nums))