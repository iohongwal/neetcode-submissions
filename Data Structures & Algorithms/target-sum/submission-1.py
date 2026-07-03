class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = []
        dp.append(0)

        for n in nums:
            nextDp = []
            for curSum in dp:
                nextDp.append(curSum + n)
                nextDp.append(curSum - n)
            dp = nextDp
        
        res = 0
        for curSum in dp:
            res = res + 1 if curSum == target else res 

        return res
