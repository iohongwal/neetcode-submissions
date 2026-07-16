class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #DP Bottom-UP
        n = len(nums)
        dp = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
            
        return max(dp)
        #DP top-down
        # dp = {}
        # def dfs(i, j):
        #     if i >= len(nums):
        #         return 0
        #     if (i, j) in dp:
        #         return dp[(i, j)]

        #     skip = dfs(i + 1, j)
        #     include = 0 
        #     if j == -1 or nums[i] > nums[j]:
        #         include = 1 + dfs(i + 1, i)
            
        #     dp[(i, j)] = max(skip, include)

        #     return dp[(i, j)]
        
        # return dfs(0, -1)
            
