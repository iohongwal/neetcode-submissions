class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #memorization
        n, m = len(s), len(t)
        cache = {}
        def backtrack(i, j):
            #base case
            if j == len(t):
                return 1

            if i >= len(s):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]
            
            if s[i] == t[j]:
                cache[(i, j)] = backtrack(i + 1, j) + backtrack(i + 1, j + 1)
            else: 
                cache[(i, j)] = backtrack(i + 1, j)

            return cache[(i, j)]

        
        return backtrack(0, 0)
        
