class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n, m = len(profit), capacity
        dp = [0] * (m + 1)

        for cap in range(weight[0], m + 1):
            if cap >= weight[0]:
                dp[cap] = profit[0]
        
        for i in range(1, n):
            curRow = [0] * (m + 1)
            for cap in range(1, m + 1):
                skip = dp[cap]
                include = 0
                if cap >= weight[i]:
                    include = profit[i] + dp[cap - weight[i]]
                curRow[cap] = max(skip, include)
            dp = curRow

        return dp[m]

