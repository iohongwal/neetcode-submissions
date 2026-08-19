class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad the array with 1s just like before
        nums = [1] + nums + [1]
        n = len(nums)
        
        # Create a 2D matrix initialized to 0
        # dp[left][right] will store the max coins for the range (left, right)
        dp = [[0] * n for _ in range(n)]
        
        # Step 1: Gradually increase the length of the sub-array we are solving
        for length in range(1, n - 1): 
            
            # Step 2: Slide a window of 'length' across the array
            for left in range(1, n - length):
                right = left + length - 1
                
                # Step 3: Try making every balloon in this window the LAST to burst
                for i in range(left, right + 1):
                    coins = nums[left - 1] * nums[i] * nums[right + 1]
                    coins += dp[left][i - 1] + dp[i + 1][right]
                    
                    dp[left][right] = max(dp[left][right], coins)
                    
        # The answer is the max coins for the full original range (1 to n-2)
        return dp[1][n - 2]