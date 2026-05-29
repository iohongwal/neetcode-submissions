class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        def graphDFS(grid, sr, sc, visited):
            nonlocal area
            if (sr >= len(grid) or sc >= len(grid[0])
                or sr < 0 or sc < 0 #Check out of bound
                or (sr, sc) in visited
                or grid[sr][sc] == 0): 
                return
            
            visited.add((sr, sc))
            
            area += 1

            graphDFS(grid, sr + 1, sc, visited)
            graphDFS(grid, sr - 1, sc, visited)
            graphDFS(grid, sr, sc + 1, visited)
            graphDFS(grid, sr, sc - 1, visited)

        
        visited = set()
        maxArea = 0

        for i in range (len(grid)):
          for j in range (len(grid[0])):
            if grid[i][j] == 1 and (i, j) not in visited:
                area = 0
                graphDFS(grid, i, j, visited)
                maxArea = max(maxArea, area)
    
        return maxArea