class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefixProduct = 1 
        suffixProduct = 1
        for i in range(len(nums)):
            res[i] *= prefixProduct
            res[len(nums) - 1 - i] *= suffixProduct

            prefixProduct *= nums[i]
            suffixProduct *= nums[len(nums) - 1 - i]
        
        return res