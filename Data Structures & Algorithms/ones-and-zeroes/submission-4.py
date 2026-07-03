class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}

        def backtrack(i, m, n):
            if (i, m, n) in dp:
                return dp[(i, m, n)]

            if i >= len(strs) or m < 0 or  n < 0:
                return 0

            #Don't pick
            skip = backtrack(i + 1, m, n)
            
            zeros, ones = 0, 0

            for c in strs[i]:
                if c == '1':
                    ones += 1
                else:
                    zeros += 1
            
            include = 0

            if zeros <= m and ones <= n:
            
                include = 1 + backtrack(i + 1, m - zeros, n - ones)
            
            length = max(skip, include)
            dp[(i, m, n)] = length

            return dp[(i, m, n)]
        
        return backtrack(0, m, n)

