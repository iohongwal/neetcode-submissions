class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        #sum method
        n = len(nums)
        return ((n * (n + 1)) // 2) - sum(nums)

        # XOR method
        # res = len(nums)
        # for i in range(len(nums)):
        #     res ^= i ^ nums[i]
        
        # return res