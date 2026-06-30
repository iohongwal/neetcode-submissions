class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        visited = set()
        min_cost = 0
        
        minHeap = [(0, 0)]

        while minHeap:
            d1, i = heapq.heappop(minHeap)

            if i in visited:
                continue
            
            min_cost += d1
            visited.add(i)

            if len(visited) == len(points):
                return min_cost
            
            x1, y1 = points[i]

            for j, [x2, y2] in enumerate(points):
                if j not in visited:
                    d2 = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(minHeap,(d2, j))
        
        return min_cost