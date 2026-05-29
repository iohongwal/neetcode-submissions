class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        # Edge Case: If the grid is empty, or start/end is blocked
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        queue = deque()
        visited = set()

        # Initialized to 1 if counting cells; change to 0 if counting steps
        length = 0

        queue.append((0,0))
        visited.add((0,0))
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return length
        
                # 4-directional movement
                neightbour = ([0,1], [0,-1], [1,0],[-1,0])
                for nr, nc in neightbour:
                    if (r + nr >= len(grid) or c + nc >= len(grid[0]) or
                        r + nr < 0 or c + nc < 0 or
                        (r + nr, c + nc) in visited or
                        grid[r + nr][c + nc] == 1
                    ):
                        continue

                    queue.append((r + nr, c + nc))
                    visited.add((r + nr, c + nc))

            length += 1
        
        return -1