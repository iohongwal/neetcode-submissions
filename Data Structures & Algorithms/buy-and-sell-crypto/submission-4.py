class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minHeap = []
        heapq.heappush(minHeap, prices[0])
        max_profit = 0
        
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - minHeap[0])
            heapq.heappush(minHeap, prices[i])
        
        return max_profit


