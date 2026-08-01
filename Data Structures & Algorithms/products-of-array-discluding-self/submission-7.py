class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefixProduct = 1
        sufferProduct = 1
    
        for i in range(len(nums)):
            #current res times the prefixProduct
            #it could skip to the product with nums[i]
            res[i] *= prefixProduct
            #compute the end res[i] with sufferProduct
            res[len(nums) - 1 - i] *= sufferProduct

            #update the prefixProduct and sufferProduct for next loop
            prefixProduct *= nums[i]
            sufferProduct *= nums[len(nums) - 1 - i]
        
        return res
