class Solution:
    def two_sum(self, nums: list, target: int) -> list:

        store = {}

        n = len(nums)

        for i in range(n):
            val = target - nums[i]
            if val in store:
                return [store[val], i]

            else:
                store[nums[i]] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    print(sol.two_sum(nums, target))