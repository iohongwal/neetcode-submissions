class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i - 1])
            max_profit = max(max_profit, prices[i] - minPrice)

        
        return max_profit