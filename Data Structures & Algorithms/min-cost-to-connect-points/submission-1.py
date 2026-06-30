class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        visited = set()
        min_cost = 0
        
        minHeap = [(0, points[0])]

        while minHeap:
            d1, [x1, y1] = heapq.heappop(minHeap)

            if (x1, y1) in visited:
                continue
            
            min_cost += d1
            visited.add((x1, y1))

            if len(visited) == len(points):
                return min_cost
            
            for x2, y2 in points:
                if (x2, y2) not in visited:
                    d2 = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(minHeap,(d2, [x2, y2]))
        
        return min_cost