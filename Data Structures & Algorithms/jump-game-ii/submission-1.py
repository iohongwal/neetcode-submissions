class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            
            if i in dp:
                return dp[i]

            dp[i] = len(nums) + 1
            for j in range(nums[i] + 1):
                dp[i] = min(dp[i], 1 + dfs(i + j))
            
            return dp[i]
        
        return dfs(0)





        
