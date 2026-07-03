class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n, m = len(profit), capacity
        dp = [[0] * (m + 1) for _ in range(n)]

        for cap in range(m + 1):
            if cap >= weight[0]:
                dp[0][cap] = profit[0]
        
        for i in range(1, n):
             for cap in range(1, m + 1):
                skip = dp[i-1][cap]
                include = 0
                if cap - weight[i] >= 0:
                    include = profit[i] + dp[i-1][cap - weight[i]]
                dp[i][cap] = max(skip, include)

        return dp[n-1][m]

