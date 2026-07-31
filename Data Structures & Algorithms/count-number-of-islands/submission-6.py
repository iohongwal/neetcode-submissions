class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()
        count = 0

        def dfs(i, j):
            if (i < 0 or j < 0 or
                i >= len(grid) or j >= len(grid[0]) or
                (i, j) in visited or grid[i][j] == "0"
            ): 
                return
            
            visited.add((i, j))

            for x, y in neighbors:
                dfs(i + x, j + y)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count     
