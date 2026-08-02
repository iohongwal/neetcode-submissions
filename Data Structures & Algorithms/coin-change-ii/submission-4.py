class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp = {}
        # def dfs(i, change):
        #     if change == 0:
        #         return 1
        #     if change < 0:
        #         return 0
        #     if i >= len(coins):
        #         return 0
        #     if (i, change) in dp:
        #         return dp[(i, change)]

        #     dp[(i, change)] = dfs(i, change - coins[i])
        #     dp[(i, change)] += dfs(i + 1, change)
            
        #     return dp[(i, change)]
            
        # return dfs(0, amount)

        dp = [[0] * (amount + 1) for _ in range(len(coins))]
        #initate dp for first coins:
        dp[0][0] = 1
        for i in range(coins[0], amount + 1):
            dp[0][i] += dp[0][i - coins[0]] 
        
        for i in range(1, len(coins)):
            dp[i][0] = 1
            for j in range(1, amount + 1):
                if j >= coins[i]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
            
        return dp[-1][-1]
