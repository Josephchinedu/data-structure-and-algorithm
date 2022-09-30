class Solution:
    def contains_duplicate(self, nums: list) -> bool:
        m = {}
        
        for i in nums:
            if i in m:
               return True
               
            else:
               m[i] = 1
        return False


if __name__ == "__main__":
    nums = [1,2,3,1]
    sol = Solution()
    print(sol.contains_duplicate(nums))