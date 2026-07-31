class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefixProduct = 1 
        suffixProduct = 1
        
        for i in range(1, len(nums)):
            prefixProduct *= nums[i - 1]
            res[i] = prefixProduct
        
        for i in range(len(nums) - 2, -1, -1):
            suffixProduct *= nums[i + 1]
            res[i] *= suffixProduct
        
        return res