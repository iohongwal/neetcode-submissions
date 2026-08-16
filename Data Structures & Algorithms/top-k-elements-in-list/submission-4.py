class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        maxHeap = []
        for num, freq in count.items():
            heapq.heappush(maxHeap, [-freq, num])
        
        res = []

        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        
        return res