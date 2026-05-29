class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        queue = deque()
        visited = set()
        length = 0

        queue.append((0,0))
        visited.add((0,0))
        
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return length
                
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