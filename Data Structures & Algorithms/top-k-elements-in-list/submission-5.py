class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        maxHeap = []

        freqs = [[] for _ in range(len(nums))]
        for num, freq in count.items():
            freqs[-freq].append(num)
            
        res = []

        for freq in freqs:
            for num in freq:
                if len(res) >= k:
                    return res
                res.append(num)
        return res