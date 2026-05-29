class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        def graphDFS(sr, sc):
            if (sr >= len(grid) or sc >= len(grid[0])
                or sr < 0 or sc < 0 #Check out of bound
                or (sr, sc) in visited
                or grid[sr][sc] == 0): 
                return 0
            
            visited.add((sr, sc))
            
            return (1 + graphDFS(sr + 1, sc)+
                graphDFS(sr - 1, sc) +
                graphDFS(sr, sc + 1) + 
                graphDFS(sr, sc - 1))

        
        visited = set()
        maxArea = 0

        for i in range (len(grid)):
          for j in range (len(grid[0])):
            if grid[i][j] == 1 and (i, j) not in visited:
                maxArea = max(maxArea, graphDFS(i, j))
    
        return maxArea