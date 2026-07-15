class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = max(nums)
        curMin, curMax = 1, 1
        
        for n in nums:
            tmp = curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(n * tmp, n * curMin, n)
            res = max(res, curMax)
        return res
