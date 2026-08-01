class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp list storaging the coin count result acroos the target amount
        dp = [float("inf")] * (amount + 1) #dp[0 to amount]
        dp[0] = 0 # 0 coins for 0 change
        
        #compute for all coins
        for coin in coins:
            for charge in range(coin, amount + 1):
                #update the dp[charge] with min counts
                dp[charge] = min(
                                    dp[charge],
                                    1 + dp[charge - coin]
                                )
        
        #return the result unless the coin is available to mark change
        return dp[-1] if dp[-1] != float("inf") else -1