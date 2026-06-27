class MedianFinder:

    def __init__(self):
        #maxHeap to return the largest small num
        self.small_nums = []
        #minHeap to return the smallest large num
        self.large_nums = []

    def addNum(self, num: int) -> None:
        #push num * -1 in to maxHeap
        heapq.heappush(self.small_nums, -1 * num)
        
        #check if the nums in small_nums is larger than the num in large_nums 
        #If yes, push the largest num in small_nums into large_nums
        if (self.small_nums and self.large_nums and 
            (-1 * self.small_nums[0]) > self.large_nums[0]):
            val = heapq.heappop(self.small_nums)
            heapq.heappush(self.large_nums, -1 * val)
        
        #handle the imbalance size between small_nums and large_nums
        if len(self.small_nums) > len(self.large_nums) + 1:
            val = heapq.heappop(self.small_nums)
            heapq.heappush(self.large_nums, -1 * val)
        if len(self.large_nums) > len(self.small_nums) + 1:
            val = heapq.heappop(self.large_nums)
            heapq.heappush(self.small_nums, -1 * val)
        

    def findMedian(self) -> float:
        if len(self.small_nums) > len(self.large_nums):
            return float(-1 * self.small_nums[0])
        elif len(self.small_nums) < len(self.large_nums):
            return float(self.large_nums[0])
        
        return (-1 * self.small_nums[0] + self.large_nums[0]) / 2