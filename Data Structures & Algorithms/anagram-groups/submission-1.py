class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)


        for s in strs:

            letterKey = [0] * 26
            for c in s:
                letterKey[ord(c) - ord('a')] += 1
            
            res[tuple(letterKey)].append(s)
        
        return list(res.values())
