class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #DP
        if len(s1) + len(s2) != len(s3):
            return False

        n, m = len(s1), len(s2)
    
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[n][m] = True

        for i in range (n, -1, -1):
            res = False
            for j in range (m, -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]


        # #memorization
        # if len(s1) + len(s2) != len(s3):
        #     return False

        # cache = {}

        # def backtrack(i, j):
        #     if i + j == len(s3):
        #         return True
            
        #     if (i, j) in cache:
        #         return cache[(i, j)]

        #     res = False
        #     if i < len(s1) and s1[i] == s3[i + j]:
        #         res = res or backtrack(i + 1, j)

        #     if j < len(s2) and s2[j] == s3[i + j]:
        #         res = res or backtrack(i, j + 1)
            
        #     cache[(i, j)] = res
        #     return res

        # return backtrack(0, 0)
            
