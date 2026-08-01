class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket approach 
        count = {}
        for n in nums:
            #update the count for that n
            count[n] = 1 + count.get(n, 0) 

        #cover the countMap to freq List
        #the index of freq list is represent the frequency of the in that row
        freq = [[] for _ in range(len(nums) + 1)]
        for key, values in count.items():
            freq[values].append(key)
        
        #out the top k elements for the freq list
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) >= k:
                    return res
                



