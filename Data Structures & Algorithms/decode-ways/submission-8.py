class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1 

        dp = {}
        def dfs(i):
            if i > len(s):
                return 0
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in dp:
                return dp[i]

            oneDigi = dfs(i + 1)
            twoDigi = 0
            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                twoDigi = dfs(i + 2) 
            dp[i] = oneDigi + twoDigi
            return dp[i]

        return dfs(0)