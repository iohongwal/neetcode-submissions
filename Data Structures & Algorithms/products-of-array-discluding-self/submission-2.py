class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        # Initialize the output array with 1s. 
        # This is crucial because we will be using multiplication to build the 
        # final answers in-place, and 1 is the multiplicative identity.
        output_product = [1] * length

        # These variables act as running accumulators. 
        # They will hold the product of all elements seen so far from the 
        # left side (prefix) and the right side (suffix).
        prefix_product = 1
        suffix_product = 1

        # We traverse the array from both ends simultaneously to save time.
        # 'i' traverses forwards: left-to-right (0 -> end)
        # '(length - 1) - i' traverses backwards: right-to-left (end -> 0)
        for i in range(length):
            
            # 1. DEPOSIT THE RUNNING PRODUCTS (Exclude Self)
            # Multiply the current running products into their respective slots.
            # We do this FIRST before updating the accumulators to ensure that
            # nums[i] is NOT included in its own prefix/suffix product.
            output_product[i] *= prefix_product
            output_product[(length - 1) - i] *= suffix_product

            # 2. UPDATE THE RUNNING PRODUCTS (Include Current)
            # Now that the output slots are safely updated, we multiply the 
            # current numbers into our running accumulators for the NEXT iteration.
            prefix_product *= nums[i]
            suffix_product *= nums[(length - 1) - i]

        return output_product