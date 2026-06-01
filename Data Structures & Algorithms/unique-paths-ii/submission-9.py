class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #edge case
        if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])

        #1D case:

        prevRow = [0] * COL
        for row in range(ROW - 1, -1, -1):
            curRow = [0] * COL
                
            if row < ROW - 1:
                curRow[COL - 1] = prevRow[COL - 1] if obstacleGrid[row][COL - 1] == 0 else 0
            else:
                curRow[COL - 1] = 1 if obstacleGrid[row][COL - 1] == 0 else 0

            for col in range(COL - 2, -1, -1):
                if obstacleGrid[row][col] == 1:
                    curRow[col] = 0
                else:
                    curRow[col] = curRow[col + 1] + prevRow[col]
            prevRow = curRow
        return prevRow[0]

