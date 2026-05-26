class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = {}
        if len(s) != len(t):
            return False
        for char in s:
            charMap[char] = charMap[char] + 1 if char in charMap else 1
        for char in t:
            if char in charMap and charMap[char] > 0:
                charMap[char] -= 1
            else:
                return False 
        return True