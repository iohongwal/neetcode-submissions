class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dsf(m, n):
            preRow = [0] * n

            for _ in range(m - 1, -1, -1):
                curRow = [0] * n
                curRow[n - 1] = 1
                for c in range(n - 2, -1, -1):
                    curRow[c]  = curRow[c + 1] + preRow[c] 
                preRow = curRow

            return preRow[0]
        return dsf(m, n)
        