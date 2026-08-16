class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        neigbhor = [[0, 1], [0,-1], [1, 0], [-1, 0]]
        res = 0
        visited = set()
        def dfs(r, c):
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] == "0" or
                (r, c) in visited
            ):
                return
            visited.add((r, c))
            #travel adjacent land
            for nr, nc in neigbhor:
                dfs(r + nr, c + nc)
            
        #iterate all lands
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    res += 1
        
        return res
