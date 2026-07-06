class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        def helper(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        for i in range(len(s)):

            res += helper(i, i) + helper(i, i + 1)
        
        return res
            

        # res = 0
        
        # for i in range(len(s)):
        #     #odd
        #     l, r = i , i
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         res += 1
        #         l -= 1
        #         r += 1

        #     #even
        #     l, r = i , i + 1
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         res += 1
        #         l -= 1
        #         r += 1

        # return res
