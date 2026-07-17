class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1

        for i in range(n - 2, -1, -1):
            num = nums[i]
            if goal == 0:
                return True

            if (num + i) >= goal:
                goal = i
            
        return True if goal == 0 else False

        # dp = {}

        # def dfs(i):
        #     if i == len(nums) - 1:
        #         return True

        #     if i >= len(nums):
        #         return False

        #     if i in dp:
        #         return dp[i]

        #     n = nums[i]

        #     if n == 0:
        #         dp[i] = False
        #         return False
            
        #     for j in range(1, n + 1):
        #         if dfs(i + j):
        #             dp[i] = True
        #             return True
            
        #     dp[i] = False
        #     return False
        
        # return dfs(0)

        
        