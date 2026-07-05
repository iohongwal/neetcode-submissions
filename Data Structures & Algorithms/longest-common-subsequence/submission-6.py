class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #DP
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    continue
                
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )
        return dp[-1][-1]
        
        # memorization
        # cache = {}

        # def backtrack(i, j):
        #     #Base case
        #     if i >= len(text1) or j >= len(text2):
        #         return 0

        #     if (i, j) in cache:
        #         return cache[(i, j)]

        #     #common letter
        #     if text1[i] == text2[j]:
        #         return 1 + backtrack(i + 1, j + 1)

        #     cache[(i, j)] = max(
        #             backtrack(i + 1, j),
        #             backtrack(i, j + 1)
        #             )

        #     return cache[(i, j)]
        
        # return backtrack(0, 0)