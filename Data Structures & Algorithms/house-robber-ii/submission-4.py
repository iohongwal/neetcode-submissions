class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(nums):
            rob1, rob2 = 0, 0

            for n in nums:
                newRob = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = newRob
            return rob2
        
        return max(helper(nums[1:]),  helper(nums[:-1]))

        ##My answer O(n)

        # if len(nums) == 1:
        #     return nums[0]
            
        # n = len(nums)
        # def backtrack(i, nums):
        #     if i >= len(nums):
        #         return 0
        #     if i in dp:
        #         return dp[i]
        #     #skip
        #     skip = backtrack(i + 1, nums)
        #     #include
        #     include = nums[i] + backtrack(i + 2, nums)

        #     dp[i] = max(skip, include)
        #     return dp[i]
        
        # dp = {}
        # res = backtrack(0, nums[:n - 1])
        # dp = {}
        # res = max(res,  backtrack(0, nums[1:n]))
        # return res