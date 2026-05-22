class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.qsortHelper(points, 0, len(points))
        return points[:k]

    def qsortHelper(self, points: List[List[int]], start, end):
        if end - start <= 1:
            return points
        pivot = points[end - 1]
        pivotD = self.pToO(pivot)
        left = start
        for i in range(start, end - 1):
            if self.pToO(points[i]) <= pivotD:
                temp = points[left]
                points[left] = points[i]
                points[i] = temp
                left += 1
        #exchange pivot and the mid element
        points[end - 1] = points[left]
        points[left] = pivot

        self.qsortHelper(points, start, left)
        self.qsortHelper(points, left + 1, end)

    #The distance between point and origin 
    def pToO (self, p1: List[int]) -> int:
        return p1[0] ** 2 + p1[1] ** 2 #((x1 - x2)^2 + (y1 - y2)^2)