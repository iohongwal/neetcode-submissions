class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = {}

        def dfs(i, j):
            if i >= len(s):
                return True

            if j >= len(t):
                return False

            if (i, j) in dp:
                return dp[(i, j)]
            
            if s[i] == t[j]:
                dp[(i, j)] = True and dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = dfs(i, j + 1)
            
            return dp[(i, j)]
        
        return dfs(0, 0)
            