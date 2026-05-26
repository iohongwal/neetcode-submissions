import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointList = []
        #Storage the dist and point
        for x, y in points:
            dist = x ** 2 + y ** 2
            pointList.append([dist, x, y])
        #heapify the pointList
        heapq.heapify(pointList)
        res = []
        while k > 0:
            res.append(heapq.heappop(pointList)[1:])
            k -= 1
        return res