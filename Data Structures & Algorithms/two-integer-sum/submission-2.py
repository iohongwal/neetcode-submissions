class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            remind = target - nums[i]
            if hashMap and remind in hashMap:
                return [hashMap[remind], i]
            
            hashMap[nums[i]] = i
        

