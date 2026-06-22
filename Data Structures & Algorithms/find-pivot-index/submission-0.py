class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        postfix_sum = [0] * (n + 1)

        prefix, postfix = 0, 0

        for i in range(n):
            prefix += nums[i]
            postfix += nums[(n - 1) - i]
            prefix_sum[i + 1] = prefix
            postfix_sum[(n - 1) - i] = postfix
        
        for i in range(n):
            if prefix_sum[i + 1] == postfix_sum[i]:
                return i

        return -1