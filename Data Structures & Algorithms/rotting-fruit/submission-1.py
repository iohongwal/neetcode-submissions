class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Edge case
        if not grid:
            return -1
        
        ROW, COL = len(grid), len(grid[0])

        visited = set()
        queue = deque()
        direction = ([0,1], [0,-1], [1,0], [-1,0]) #horizontal and vertical
        #Find the rotten friut;
        freshFriut =  0
        for i in range(ROW):
            for j in range(COL):
                #check if fruit is rotted or visited
                if grid[i][j] == 2 or (i, j) in visited:
                    queue.append((i,j))
                    visited.add((i,j))
                if grid[i][j] == 1:
                    freshFriut += 1
                
        minutes = 0
        while queue and freshFriut > 0:
            minutes += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for r, c in direction:
                    nextRow, nextCol = row + r, col + c
                    if (nextRow < 0 or nextCol < 0 or 
                        nextRow >= ROW or nextCol >= COL #Check if out of bound
                        or (nextRow, nextCol) in visited
                        or grid[nextRow][nextCol] != 1
                        ):
                        continue

                    queue.append((nextRow,nextCol))
                    visited.add((nextRow,nextCol))
                    freshFriut -= 1
                            
        return minutes if freshFriut == 0 else -1