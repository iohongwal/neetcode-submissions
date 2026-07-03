class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #DP
        dp = defaultdict(int)

        for s in strs:
            zeros, ones = s.count("0"), s.count("1")
            for zero in range(m, zeros - 1, -1):
                for one in range(n, ones - 1, -1):
                    dp[(zero, one)] = max(
                        1 + dp[(zero - zeros, one - ones)], 
                        dp[(zero, one)]
                    )
        return dp[(m, n)]
        
        #Memoization method
        # dp = {}

        # def backtrack(i, m, n):
        #     #Base case
        #     if i >= len(strs):
        #         return 0
        #     #cache check
        #     if (i, m, n) in dp:
        #         return dp[(i, m, n)]

        #     #Don't pick
        #     dp[(i, m, n)] = backtrack(i + 1, m, n)
            
        #     #Pick
        #     zeros = strs[i].count('0')
        #     ones = len(strs[i]) - zeros

        #     if zeros <= m and ones <= n:
            
        #         dp[(i, m, n)] = max(
        #             dp[(i, m, n)],
        #             1 + backtrack(i + 1, m - zeros, n - ones))

        #     return dp[(i, m, n)]
        
        # return backtrack(0, m, n)

