class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        if totalSum %2 != 0:
            return False
        
        halfSum = totalSum // 2
        
        dp = set()
        dp.add(0)

        for i in range(len(nums) -1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == halfSum:
                    return True
                nextDP.add(t) #Skip
                nextDP.add(t + nums[i]) #include
            dp = nextDP

        return True if halfSum in dp else False