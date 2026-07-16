class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #DP Bottom-up
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (len(s) >= (i + len(w))) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]

        #Dp top-down
        # dp = {}
        # def dfs(i):
        #     if i == len(s):
        #         return True
        #     if i in dp:
        #         return dp[i]
            
        #     for w in wordDict:
        #         if s[i : i + len(w)] == w:
        #             if dfs(i + len(w)):
        #                 dp[i] = True
        #                 return True

        #     dp[i] = False
        #     return False
        
        # return dfs(0)
            
            