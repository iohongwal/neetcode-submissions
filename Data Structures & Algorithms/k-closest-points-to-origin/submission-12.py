class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.quickSelect(points, 0, len(points) - 1, k)
        return points[:k]

    def quickSelect(self, points: List[List[int]], start, end, k):
        if end - start < 1:
            return
        pivot_idx = self.qsPartition(points, start, end)

        if pivot_idx == k:
            return
        elif pivot_idx < k:
            # The k is in the Right, the system only need to sort the Right side 
            self.quickSelect(points, pivot_idx + 1, end, k)
        else: 
            # The k is in the Left, the system only need to sort the left side 
            self.quickSelect(points, start, pivot_idx - 1, k)

    def qsPartition(self, points: List[List[int]], start, end) -> int:
        pivot = points[end]
        pivotD = self.pToO(pivot)
        left = start
        for i in range(start, end):
            if self.pToO(points[i]) <= pivotD:
                temp = points[left]
                points[left] = points[i]
                points[i] = temp
                left += 1
        #exchange pivot and the mid element
        points[end], points[left] = points[left], pivot
        return left

    #The distance between point and origin 
    def pToO (self, p1: List[int]) -> int:
        return p1[0] ** 2 + p1[1] ** 2 #((x1 - x2)^2 + (y1 - y2)^2)