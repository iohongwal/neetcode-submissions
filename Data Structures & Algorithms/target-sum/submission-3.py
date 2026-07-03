class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if total < target:
            return 0

        dp = {}

        def backtrack(i, curSum):
            if (i, curSum) in dp:
                return dp[(i, curSum)]
            
            if i == len(nums):
                return 1 if curSum == target else 0
            
            dp[(i, curSum)] = (
                backtrack(i + 1, curSum + nums[i]) +
                backtrack(i + 1, curSum - nums[i])
            )
            return dp[(i, curSum)]

        return backtrack(0, 0)

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
