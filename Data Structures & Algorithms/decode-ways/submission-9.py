class Solution:
    def numDecodings(self, s: str) -> int:
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
            
            dp[i] = dfs(i + 1)
            if i + 1 < len(s) and int(s[i:i+2]) < 27:
                dp[i] += dfs(i + 2)
            
            return dp[i]
        
        return dfs(0)