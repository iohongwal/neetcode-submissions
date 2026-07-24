class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        res = []
        L = 0

        for R in range(len(nums)):
            window.append(nums[R])
            if R - L + 1 >= k:
                res.append(max(window))
                window.popleft()
                L += 1
            
        
        return res
                