class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        #initiate the dp[m - 1][0...n - 1] and dp[0...m - 1][n - 1]
        #It is because it have only one way to reach bottom-right corner from either the last row or the last column except out of bound as the requirement mentioned we go only to down or right

        #initiate the last row except out of bound
        for i in range(n):
            dp[m - 1][i] = 1
        
        #initiate the last column except out of bound
        for i in range(m):
            dp[i][n - 1] = 1
        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        
        return dp[0][0]