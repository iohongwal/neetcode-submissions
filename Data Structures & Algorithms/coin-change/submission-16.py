class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0 
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(
                    1 + dp[i - coin],
                    dp[i]
                )

        return dp[-1] if dp[-1] != float("inf") else -1