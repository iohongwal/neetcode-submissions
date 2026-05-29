class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #Edage case
        ROW, COL = len(grid), len(grid[0])
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        minPath = sys.maxsize
        queue = deque()
        visited = set()

        queue.append((0,0))
        visited.add((0,0))
        length = 1
        Path = False

        #8-directionall
        neighbour = ([0,1], [0,-1], [1,0], [-1,0], 
                    [1,1], [-1,-1], [1,-1], [-1,1])
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                #Reached bottom-right
                if row == ROW - 1 and col == COL - 1:
                    minPath = min(minPath, length)
                    Path = True

                for r, c in neighbour:
                    nextRow, nextCol = row + r, col + c
                    
                    if (nextRow < 0 or nextCol < 0 or nextRow >= ROW or nextCol >= COL #check if out of bound
                        or (nextRow, nextCol) in visited #Check if visited
                        or grid[nextRow][nextCol] == 1 #Check if hit well
                    ):
                        continue
                    
                    queue.append((nextRow,nextCol))
                    visited.add((nextRow,nextCol))

            length += 1

        return minPath if Path else -1


