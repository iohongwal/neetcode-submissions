class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profix = 0
        for i in range(len(prices)):
            j = i + 1
            while j < len(prices) and prices[j] > prices[i]:
                profix = max(prices[j] - prices[i], profix)
                j += 1
            i = j
        
        return profix
                
        

