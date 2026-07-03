class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if total < target:
            return 0

        #1d dp method
        dp = defaultdict(int)
        dp[0] = 1 #0 sum -> 1 way

        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                next_dp[cur_sum + nums[i]] += count
                next_dp[cur_sum - nums[i]] += count
            dp = next_dp
        
        return dp[target]

        #2d dp method

        # dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        # #(0 elements, 0 sum) -> 1 way
        # #1 way to sum to zero with first 0 elements
        # dp[0][0] = 1 

        # for i in range(len(nums)):
        #     for cur_sum, count in dp[i].items():
        #         dp[i + 1][cur_sum + nums[i]] += count
        #         dp[i + 1][cur_sum - nums[i]] += count
        
        # return dp[-1][target]

        #memorize method

        # dp = {}

        # def backtrack(i, curSum):
        #     if (i, curSum) in dp:
        #         return dp[(i, curSum)]
            
        #     if i == len(nums):
        #         return 1 if curSum == target else 0
            
        #     dp[(i, curSum)] = (
        #         backtrack(i + 1, curSum + nums[i]) +
        #         backtrack(i + 1, curSum - nums[i])
        #     )
        #     return dp[(i, curSum)]

        # return backtrack(0, 0)

        # dp = []
        # dp.append(0)

        # for n in nums:
        #     nextDp = []
        #     for curSum in dp:
        #         nextDp.append(curSum + n)
        #         nextDp.append(curSum - n)
        #     dp = nextDp
        
        # res = 0
        # for curSum in dp:
        #     res = res + 1 if curSum == target else res 

        #return res
