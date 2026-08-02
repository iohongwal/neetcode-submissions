class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        neigbhor = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queen = deque()
        minutes = 0
        fresh = 0
        #find all rotted orange in the griven grid:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queen.append([i,j])
        
        while queen and fresh > 0:

            for _ in range(len(queen)):
                i, j = queen.popleft()

                for x, y in neigbhor:
                    newX, newY = i + x, j + y
                    if (0 <= newX < len(grid) and
                        0 <= newY < len(grid[0]) and 
                        grid[newX][newY] == 1):
                        grid[newX][newY] = 2
                        fresh -= 1
                        queen.append([newX,newY])
                        
            
            minutes += 1

        return minutes if fresh == 0 else -1
