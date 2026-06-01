class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #edge case
        if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])
        if ROW == 1 or COL == 1:
            for row in range(ROW):
                for col in range(COL):
                    if obstacleGrid[row][col] == 1:
                        return 0
            return 1
                
        dp = [[0]*COL for _ in range(ROW)]

        dp[-1][-1] = 1

        #last row route
        for col in range(COL - 2, -1, -1):
            dp[-1][col] = dp[-1][col + 1] if obstacleGrid[-1][col] == 0 else 0

        #last col route
        for row in range(ROW - 2, -1, -1):
            dp[row][-1] = dp[row + 1][-1] if obstacleGrid[row][-1] == 0 else 0 

        for row in range(ROW - 2, -1, -1):
            for col in range(COL - 2, -1, -1):
                dp[row][col] = dp[row + 1][col] + dp[row][col + 1] if obstacleGrid[row][col] == 0 else 0 

        return dp[0][0]
