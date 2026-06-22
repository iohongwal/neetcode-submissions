class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix_sum = 0

        for i in range(len(nums)):
            n = nums[i]
            if total - prefix_sum - n == prefix_sum:
                return i
            prefix_sum += n

        return -1