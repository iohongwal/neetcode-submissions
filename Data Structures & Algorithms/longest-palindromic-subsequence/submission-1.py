class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        cache = {}
        def helper(l, r):
            #odd case: s[l] == s[r] return 1
            if l == r:
                return 1
            #even case: s[l] != s[r] return 1
            if l > r: 
                return 0
            
            if (l, r) in cache:
                return cache[(l, r)]

            if s[l] == s[r]:
                cache[(l, r)] = 2 + helper(l + 1, r - 1)
                return cache[(l, r)]
            
            cache[(l, r)] = max(helper(l + 1, r), helper(l, r - 1))
            
            return cache[(l, r)]

        return helper(0, len(s) - 1)