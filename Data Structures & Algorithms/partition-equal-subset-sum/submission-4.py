class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        if totalSum %2 != 0:
            return False
        
        halfSum = totalSum // 2
        
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            if nums[i] == halfSum:
                return True
            nextDP = set()
            for t in dp:
                nextDP.add(t) #Skip
                nextDP.add(t + nums[i]) #include
            dp = nextDP

        return True if halfSum in dp else False