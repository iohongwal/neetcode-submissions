class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0 : 1}
        prefix_sum = 0
        res = 0
        for n in nums:
            prefix_sum += n
            diff = prefix_sum - k
            
            res += prefix_sums.get(diff, 0)

            prefix_sums[prefix_sum] = 1 + prefix_sums.get(prefix_sum, 0)


        return res