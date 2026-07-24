class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() #contain index
        l = r = 0

        while r < len(nums):
            #pop smaller values from q
            while q and nums[q[-1]] < nums[r]: 
                q.pop()
            q.append(r)

            #remove left val from window
            if l > q[0]:
                q.popleft()
            
            if r - l + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        
        return res
        

        # window = deque()
        # res = []
        # L = 0

        # for R in range(len(nums)):
        #     window.append(nums[R])
        #     if R - L + 1 >= k:
        #         res.append(max(window))
        #         window.popleft()
        #         L += 1
            
        
        # return res
                