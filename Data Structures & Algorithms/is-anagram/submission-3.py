class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letterCount = [0] * 26
        for c in s:
            letterCount[ord(c) - ord("a")] += 1
        for c in t:
            if letterCount[ord(c) - ord("a")] < 1:
                return False
            
            letterCount[ord(c) - ord("a")] -= 1
        
        return True
        
        