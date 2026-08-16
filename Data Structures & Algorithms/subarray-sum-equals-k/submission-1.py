class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixs = {0:1}
        prefix = 0
        res = 0
        for n in nums:
            prefix += n
            diff = prefix - k

            res += prefixs.get(diff, 0)
            prefixs[prefix] = prefixs.get(prefix, 0) + 1
            
            
        
        return res