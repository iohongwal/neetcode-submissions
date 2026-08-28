class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hashMap = {} # letter : last_index
        for i in range(len(s)):
            hashMap[s[i]] = max(i, hashMap.get(s[i], 0))

        res = []

        l = r = 0
        for i in range(len(s)):
            end_idx = hashMap[s[i]]
            if r < end_idx:
                r = end_idx
            
            if i == r:
                res.append(r - l + 1)
                l = r = i + 1
        
        return res
            
        
