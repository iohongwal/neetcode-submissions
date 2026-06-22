class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output_product = [1] * length

        prefix_product = 1
        suffix_product = 1

        for i in range(length):
            output_product[i] *= prefix_product
            output_product[(length - 1) - i] *= suffix_product

            prefix_product *= nums[i]
            suffix_product *= nums[(length - 1) - i]


        return output_product
