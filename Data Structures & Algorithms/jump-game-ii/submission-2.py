class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        #initall position
        l = r = 0 #l last step, r next step

        #loop until r reach the last position
        while r < len(nums) - 1:
            
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            l = r + 1
            r = farthest
            res += 1
        
        return res

        
        # dp = {}
        # def dfs(i):
        #     if i >= len(nums) - 1:
        #         return 0
            
        #     if i in dp:
        #         return dp[i]

        #     dp[i] = len(nums) + 1
        #     for j in range(nums[i] + 1):
        #         dp[i] = min(dp[i], 1 + dfs(i + j))
            
        #     return dp[i]
        
        # return dfs(0)





        
