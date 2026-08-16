class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        l = 0
        substring = set()
        for r in range(len(s)):

            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            
            substring.add(s[r])
            maxLength = max(maxLength, (r - l + 1))

        return maxLength
                 
                