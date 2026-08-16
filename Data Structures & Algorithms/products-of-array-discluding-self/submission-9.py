class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1, 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            
            res[i] *= pre
            res[len(nums) - 1 - i] *= post

            pre *= nums[i]
            post *= nums[len(nums) - 1 - i]
        
        return res
        