class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        # Edge Case: If the grid is empty, or start/end is blocked
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        ROW, COL = len(grid), len(grid[0])
        queue = deque()
        visited = set()

        # Initialized to 1 if counting cells; change to 0 if counting steps
        length = 0

        queue.append((0,0))
        visited.add((0,0))
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROW - 1 and c == COL - 1:
                    return length
        
                # 4-directional movement
                neightbour = ([0,1], [0,-1], [1,0],[-1,0])

                for nr, nc in neightbour:
                    newR, newC = r + nr, c + nc
                    if (newR >= ROW or newC >= COL or
                        newR < 0 or newC < 0 or
                        (newR, newC) in visited or
                        grid[newR][newC] == 1
                    ):
                        continue

                    queue.append((newR, newC))
                    visited.add((newR, newC))

            length += 1
        
        return -1