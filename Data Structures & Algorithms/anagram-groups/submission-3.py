class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaragms = collections.defaultdict(list)
        
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord("a")] += 1
            anaragms[tuple(counter)].append(s)
        
        return list(anaragms.values())
        