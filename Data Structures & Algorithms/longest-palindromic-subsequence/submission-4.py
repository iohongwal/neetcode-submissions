class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        #LCS DP
        n = len(s)

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s[n - j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1]

        #LCS Cache
        # cache = {}
        # def helper(l, r):
        #     #odd case: s[l] == s[r] return 1
        #     if l == r:
        #         return 1
        #     #even case: s[l] != s[r] return 1
        #     if l > r: 
        #         return 0
            
        #     if (l, r) in cache:
        #         return cache[(l, r)]

        #     if s[l] == s[r]:
        #         cache[(l, r)] = 2 + helper(l + 1, r - 1)
        #         return cache[(l, r)]
            
        #     cache[(l, r)] = max(helper(l + 1, r), helper(l, r - 1))

        #     return cache[(l, r)]

        # return helper(0, len(s) - 1)

        # cache = {}
        # def dfs (l, r):
        #     if l < 0 or r >= len(s):
        #         return 0
            
        #     if (l, r) in cache:
        #         return cache[(l, r)]
            
        #     if s[l] == s[r]:
        #         length = 1 if l == r else 2
        #         cache[(l, r)] = length + dfs (l - 1, r + 1)
        
        #     else:
        #         cache[(l, r)] = max(dfs(l - 1, r), dfs(l, r + 1))

        #     return cache[(l, r)]
        
        # for i in range(len(s)):
        #     dfs(i, i)
        #     dfs(i, i + 1)

        # return max(cache.values())
        
