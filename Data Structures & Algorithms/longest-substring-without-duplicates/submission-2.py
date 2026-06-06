class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, length = 0, 0
        substring = ""

        for R in range(len(s)):

            while s[R] in substring:
                substring = substring.replace(s[L], "")
                L += 1

            substring += s[R]
            length = max(length, R - L + 1)
        
        return length