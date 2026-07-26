class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashSet = set()
        maxHeap = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            heapq.heappush(maxHeap,(-position[i], time))

        prevTime = 0
        while maxHeap:
            curCar, curTime = heapq.heappop(maxHeap)
            curCar = -curCar

            if curTime > prevTime:
                hashSet.add(curTime)
                prevTime = curTime
            
        return len(hashSet)