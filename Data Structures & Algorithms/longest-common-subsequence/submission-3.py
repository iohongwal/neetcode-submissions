class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        I, J = len(text1), len(text2)
        dp = [[0] * (J + 1) for _ in range(I + 1)]
        
        x = -1
        for i in range(I - 1, -1, -1):
            for j in range(J - 1, -1, -1):
                if text1[i] != text2[j]:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                else:
                    dp[i][j] =  1 + dp[i + 1][j + 1]

        return dp[0][0]