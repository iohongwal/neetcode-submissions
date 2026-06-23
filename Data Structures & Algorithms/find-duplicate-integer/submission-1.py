class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = None

        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                res = abs(nums[i])
                break
            nums[abs(nums[i]) - 1] *= -1

        return res