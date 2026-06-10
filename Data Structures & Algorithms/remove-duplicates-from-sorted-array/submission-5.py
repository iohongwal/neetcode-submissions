class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) < 1: return 1

        L = 1
        
        for R in range(1, len(nums)):
            if nums[R - 1] != nums[R]:
                nums[L] = nums[R]
                L += 1

        return L
