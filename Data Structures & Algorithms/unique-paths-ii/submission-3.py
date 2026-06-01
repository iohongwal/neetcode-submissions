class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #edge case
        if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])
        def dfs(ROW, COL):
            prevRow = [0] * COL

            for row in range(ROW - 1, -1, -1):
                curRow = [0] * COL
                curRow[COL - 1] = 1 if obstacleGrid[row][COL - 1] == 0 else 0
                if row < ROW - 1 and prevRow[COL - 1] == 0:
                    curRow[COL - 1] = 0

                for col in range(COL - 2, -1, -1):
                    if obstacleGrid[row][col] == 1:
                        curRow[col] = 0
                    else:
                        curRow[col] = curRow[col + 1] + prevRow[col]
                prevRow = curRow
            return prevRow[0]
        return dfs(ROW, COL)
