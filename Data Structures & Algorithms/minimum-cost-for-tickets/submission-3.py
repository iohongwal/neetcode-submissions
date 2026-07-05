class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # DP
        dp = [float("inf")] * len(days)
        
        for i in range(len(days)):
            for cost, duration in zip(costs, [1, 7, 30]):
                j = i - 1
                while j >= 0 and days[j] > days[i] - duration:
                    j -= 1
                
                past_cost = dp[j] if j >= 0 else 0
                dp[i] = min(dp[i], cost + past_cost)
        
        return dp[-1]

        # #memorization

        # dp = {}

        # def dfs(i):
        #     if i == len(days):
        #         return 0
            
        #     if i in dp:
        #         return dp[i]

        #     dp[i] = float("inf")
        #     j = i
        #     for cost, duration in zip(costs, [1, 7, 30]):
        #         while j < len(days) and days[j] < days[i] + duration:
        #             j += 1
        #         dp[i] = min(dp[i], cost + dfs(j))
            
        #     return dp[i]
        
        # return dfs(0)