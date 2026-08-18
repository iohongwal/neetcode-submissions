class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        neigbhor = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dp = {}
        self.maxLen = 0

        def dfs(r, c, lastVal):
            if (
                r < 0 or c < 0 or 
                r >= len(matrix) or c >= len(matrix[0]) or 
                matrix[r][c] <= lastVal
            ):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            for dr, dc in neigbhor:
                res = max(res, 1 + dfs(r + dr, c + dc, matrix[r][c]))
            
            dp[(r, c)] = res
            self.maxLen = max(res, self.maxLen)
            return dp[(r, c)]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                dfs(r, c, -1)
        return self.maxLen