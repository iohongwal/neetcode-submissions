class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp[0...amount] store the num of coin alogn the amount
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        #initiate the dp array with the first coin
        for charge in range(coins[0], amount + 1):
            dp[charge] = 1 + dp[charge - coins[0]]
        
        for i in range(1, len(coins)):
            for charge in range(coins[i], amount + 1):
                dp[charge] = min(
                            1 + dp[charge - coins[i]],
                            dp[charge]
                            )

        return dp[-1] if dp[-1] != float("inf") else -1
