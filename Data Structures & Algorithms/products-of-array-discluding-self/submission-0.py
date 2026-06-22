class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix_products = [1] * length
        suffix_products = [1] * length 
        output_product = [0] * length

        prefix_product = 1
        suffix_product = 1

        for i in range(length):
            prefix_product *= nums[i]
            suffix_product *= nums[(length - 1) - i]
            prefix_products[i] = prefix_product
            suffix_products[(length - 1) - i] = suffix_product

        for i in range(length):
            prefix = prefix_products[i - 1] if i > 0 else 1
            suffix = suffix_products[i + 1] if i < (length - 1) else 1
            output_product[i] = prefix * suffix
        
        return output_product
