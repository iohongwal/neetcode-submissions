class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for n in nums:
            if n in hashMap:
                hashMap[n] -= 1
            else:
                hashMap[n] = -1

        maxHeap = []

        for key, value in hashMap.items():
            heapq.heappush(maxHeap, (value, key))

        res = []

        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        
        return res