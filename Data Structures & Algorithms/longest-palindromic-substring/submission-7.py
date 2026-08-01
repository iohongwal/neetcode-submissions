class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        startIdx = 0 
        for i in range(len(s)):

            #odd case:
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) + 1 > maxLength:
                    maxLength = (r - l) + 1
                    startIdx = l
                l -= 1
                r += 1
                
            
            #even case:
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) + 1 > maxLength:
                    maxLength = (r - l) + 1
                    startIdx = l
                l -= 1
                r += 1
            
        return s[startIdx: startIdx + maxLength]