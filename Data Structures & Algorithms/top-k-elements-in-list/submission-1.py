class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Bucket apporach
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for key, value in count.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
    
        #MaxHeap apporch
        # hashMap = {}

        # for n in nums:
        #     if n in hashMap:
        #         hashMap[n] -= 1
        #     else:
        #         hashMap[n] = -1

        # maxHeap = []

        # for key, value in hashMap.items():
        #     heapq.heappush(maxHeap, (value, key))

        # res = []

        # for _ in range(k):
        #     res.append(heapq.heappop(maxHeap)[1])
        
        # return res