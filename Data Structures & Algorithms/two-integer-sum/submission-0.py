class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, num in enumerate(nums):
            if (target - num) in numMap:
                return [nums.index(target - num), i]
            else: 
                numMap[num] = 1
                
        return None
             