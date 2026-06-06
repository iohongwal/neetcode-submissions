class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total, length, L = 0, len(nums) + 1, 0

        for R in range(len(nums)):
            total += nums[R]

            while total >= target:
                length = min(R - L + 1, length)
                total -= nums[L]
                L += 1

        return 0 if length == len(nums) + 1 else length
                