class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, length = 0, 0
        substring = set()

        for R in range(len(s)):

            while s[R] in substring:
                substring.remove(s[L])
                L += 1

            substring.add(s[R])
            length = max(length, R - L + 1)
        
        return length