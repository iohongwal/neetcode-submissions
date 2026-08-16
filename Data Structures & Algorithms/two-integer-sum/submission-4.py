class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            n = nums[i]
            if (target - n) in hashMap:
                return [hashMap[(target - n)], i]

            hashMap[ n] = i
        
        return None