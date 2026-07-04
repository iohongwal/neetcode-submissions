class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        #DP Button-up
        n = len(profit)

        #dp[0...n-1][0...8]
        dp = [[0] * (capacity + 1) for _ in range(n)]
        
        for c in range(capacity + 1):
            if c >= weight[0]:
                dp[0][c] = profit[0] + dp[0][c - weight[0]]

        for i in range(1, n):
            for c in range(1, capacity + 1):
                skip = dp[i - 1][c]
                include = 0
                if c >= weight[i]:
                    include = profit[i] + dp[i][c - weight[i]]
                dp[i][c] = max(skip, include)

        return dp[-1][-1]
        