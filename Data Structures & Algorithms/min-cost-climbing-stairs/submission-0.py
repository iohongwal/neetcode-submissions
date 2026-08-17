class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 2)
        dp[1] = cost[0] 
        for i in range(2, len(cost) + 2):
            dp[i] = min(dp[i - 1], dp[i - 2])
            if i - 1 < len(cost):
                dp[i] += cost[i - 1]
        
        return dp[-1]