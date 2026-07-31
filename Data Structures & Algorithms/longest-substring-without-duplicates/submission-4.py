class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        l = 0
        subStr = set()
        for r in range(len(s)):
            while s[r] in subStr:
                subStr.remove(s[l])
                l += 1
            
            subStr.add(s[r])
            maxLength = max(maxLength, (r - l) + 1)

        return maxLength
                
