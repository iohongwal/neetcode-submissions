class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # memorization
        cache = {}

        def backtrack(i, j):
            #Base case
            if i >= len(text1) or j >= len(text2):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            #common letter
            if text1[i] == text2[j]:
                return 1 + backtrack(i + 1, j + 1)

            cache[(i, j)] = max(
                    backtrack(i + 1, j),
                    backtrack(i, j + 1)
                    )

            return cache[(i, j)]
        
        return backtrack(0, 0)