class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        
        for i in range(len(nums)):
            missing += i #sum of 0 to n
            missing -= nums[i] #mins sum of array

        return missing