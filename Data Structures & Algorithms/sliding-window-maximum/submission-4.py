class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #MaxHeap soluation
        res = []
        window = []

        #First window
        for i in range(k):
            heapq.heappush(window, (-nums[i], i))
        
        #Append the maximum in first window to res
        res.append(-window[0][0])

        #Iterate another windows
        for i in range(k, len(nums)):
            heapq.heappush(window, (-nums[i], i))

            #Pop the out of window item
            while window[0][1] <= i - k:
                heapq.heappop(window)
            
            res.append(-window[0][0])
        
        return res

        # res = []
        # q = deque() #contain index
        # l = r = 0

        # while r < len(nums):
        #     #pop smaller values from q
        #     while q and nums[q[-1]] < nums[r]: 
        #         q.pop()
        #     q.append(r)

        #     #remove left val from window
        #     if l > q[0]:
        #         q.popleft()
            
        #     if r - l + 1 >= k:
        #         res.append(nums[q[0]])
        #         l += 1
        #     r += 1
        
        # return res
        

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
                