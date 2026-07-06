class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        dp = [[""] * (m + 1) for _ in range(n + 1)]

        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i >= n:
                    dp[i][j] = str2[j:]
                elif j >= m:
                    dp[i][j] = str1[i:]
                elif str1[i] == str2[j]:
                    dp[i][j] = str1[i] + dp[i + 1][j + 1]
                else:
                    res1 = str1[i] + dp[i + 1][j]
                    res2 = str2[j] + dp[i][j + 1]
                    dp[i][j] = res1 if len(res1) < len(res2) else res2

        return dp[0][0]

        # #memorization
        # cache = {}

        # def bracktrack(i, j):
        #     if i == len(str1):
        #         return str2[j:]
            
        #     if j == len(str2):
        #         return str1[i:]
            
        #     if (i, j) in cache:
        #         return cache[(i, j)]

        #     if str1[i] == str2[j]:
        #         return str1[i] + bracktrack(i + 1, j + 1)

            
        #     res1 = str1[i] + bracktrack(i + 1, j)
        #     res2 = str2[j] + bracktrack(i, j + 1)

        #     if len(res1) < len(res2):
        #         cache[(i, j)] = res1
        #         return res1

        #     cache[(i, j)] =  res2

        #     return res2

        # return bracktrack(0, 0)
                