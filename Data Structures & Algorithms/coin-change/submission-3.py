class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0

        n = len(coins)

        #dp[0...n-1]][0...amount]
        dp = [[float('inf')] * (amount + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 0

        for change in range(coins[0], amount + 1):
            dp[0][change] = 1 + dp[0][change - coins[0]]

        for i in range(1, n):
            for change in range(1 , amount + 1):
                dp[i][change] = dp[i - 1][change]
                if change >= coins[i]:
                    dp[i][change] = min(
                        dp[i][change], 
                        1 + dp[i][change - coins[i]]
                        )
        
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
