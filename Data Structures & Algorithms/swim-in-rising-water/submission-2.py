class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        visited = set()
        minHeap = [(grid[0][0], (0, 0))]
        minTime = 0
        n, m = len(grid), len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while minHeap:
            t1, (i, j) = heapq.heappop(minHeap)
            
            if (i, j) in visited:
                continue

            visited.add((i, j))
            minTime = max(minTime, t1)

            if i == n - 1 and j == m - 1:
                return minTime

            for dx, dy in directions:
                nxt_i, nxt_j = i + dx, j + dy
                if (nxt_i >= 0 and nxt_j >= 0
                    and nxt_i < n and nxt_j < n
                    and (nxt_i, nxt_j) not in visited):
                    heapq.heappush(minHeap, (grid[nxt_i][nxt_j], (nxt_i, nxt_j)))


        return minTime