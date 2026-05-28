class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        def graphDFS(grid, row, col, visited) -> int:
            ROW, COL = len(grid), len(grid[0])
            if (row >= ROW or col >= COL or min(row, col) < 0 #out of bound
                or grid[row][col] == 1 #hit rock 
                or (row, col) in visited): #visited
                return 0
            if row == ROW - 1 and col == COL - 1: #Reached the bottom-right corner 
                return 1
            
            visited.add((row, col)) #Add the node to visited list

            counter = 0 #count the number of tour that reach the bottom-right corner
            counter += graphDFS(grid, row + 1, col, visited) #go down
            counter += graphDFS(grid, row - 1, col, visited) #go up
            counter += graphDFS(grid, row, col + 1, visited) #go right
            counter += graphDFS(grid, row, col - 1, visited) #go left

            visited.remove((row, col)) #Remove the node to visited list

            return counter

        return graphDFS(grid, 0, 0, set())

