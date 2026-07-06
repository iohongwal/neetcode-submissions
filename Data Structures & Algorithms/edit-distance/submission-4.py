class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #DP bottom-up
        n, m = len(word1), len(word2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = i

        for j in range(m + 1):
            dp[0][j] = j
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j - 1],
                        dp[i - 1][j],
                        dp[i - 1][j - 1]
                    )

        return dp[-1][-1]

        # #memorization
        # cache = {}

        # def backtrack(i, j):
        #     if i >= len(word1):
        #         #return num of insert operations
        #         return len(word2) - j
                
        #     if j >= len(word2):
        #         #return num of delet operations
        #         return len(word1) - i
            
        #     if (i, j) in cache:
        #         return cache[(i, j)]

        #     if word1[i] == word2[j]:
        #         return backtrack(i + 1, j + 1)

        #     cache[(i, j)] = 1 + min(
        #         # insert the character at the current index of word1
        #         backtrack(i, j + 1), 
        #         # delete the current character of word1
        #         backtrack(i + 1, j),
        #         # replace the character at index i
        #         backtrack(i + 1, j + 1)
        #         )

        #     return cache[(i, j)]
            
        
        # return backtrack(0, 0)