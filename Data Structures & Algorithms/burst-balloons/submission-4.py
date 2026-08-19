class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        def bucktrack(nums):
            if len(nums) == 0:
                return 0
            if tuple(nums) in dp:
                return dp[tuple(nums)]
            
            dp[tuple(nums)] = 0
            for i in range(len(nums)):
                left = nums[i - 1] if i > 0 else 1
                right = nums[i + 1] if i < len(nums) - 1 else 1 
                coins = left * nums[i] * right

                coins += bucktrack(nums[:i] + nums[i + 1:])
                dp[tuple(nums)] = max(dp[tuple(nums)], coins)
            
            return dp[tuple(nums)]
            
        return bucktrack(nums)

               
