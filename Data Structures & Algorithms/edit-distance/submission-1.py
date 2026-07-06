class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #memorization
        cache = {}

        def backtrack(i, j):
            if i >= len(word1):
                return len(word2) - j
                
            if j >= len(word2):
                return len(word1) - i
            
            if (i, j) in cache:
                return cache[(i, j)]

            if word1[i] == word2[j]:
                return backtrack(i + 1, j + 1)

            cache[(i, j)] = 1 + min(
                backtrack(i + 1, j),
                backtrack(i, j + 1),
                backtrack(i + 1, j + 1)
                )

            return cache[(i, j)]
            
        
        return backtrack(0, 0)