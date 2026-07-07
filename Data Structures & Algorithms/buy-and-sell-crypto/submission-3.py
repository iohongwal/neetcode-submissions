class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        max_profit = 0
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)
            if profit < 0:
                buy += 1
                sell = buy + 1
            else:
                sell += 1
        return max_profit

        # max_profit = 0
        # minPrice = prices[0]
        # for i in range(1, len(prices)):
        #     minPrice = min(minPrice, prices[i - 1])
        #     max_profit = max(max_profit, prices[i] - minPrice)
        # return max_profit