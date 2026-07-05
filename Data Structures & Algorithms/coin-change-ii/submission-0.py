class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 1. Initialize with 0s (we are counting!)
        dp = [0] * (amount + 1)
        
        # 2. Base case: There is 1 way to make $0 (use zero coins)
        dp[0] = 1
        
        for coin in coins:
            # 3. Unbounded Knapsack: Iterate FORWARDS
            for change in range(coin, amount + 1):
                # 4. The Magic: Add the ways we can reach this amount using the coin!
                dp[change] += dp[change - coin]
                
        return dp[amount]
        



        