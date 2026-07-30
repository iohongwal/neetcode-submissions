class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        for r in range(1, len(prices)):
            while prices[l] > prices[r]:
                l += 1
            max_profit = max(max_profit, prices[r] - prices[l])
        
        return max_profit
        
        #O(nlogn)
        # minHeap = []
        # heapq.heappush(minHeap, prices[0])
        # max_profit = 0
        
        # for i in range(1, len(prices)):
        #     max_profit = max(max_profit, prices[i] - minHeap[0])
        #     heapq.heappush(minHeap, prices[i])
        
        # return max_profit


