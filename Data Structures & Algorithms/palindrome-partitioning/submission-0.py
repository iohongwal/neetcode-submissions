class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
    
        def backtrack(i, palindromes):
            if i >= len(s):
                res.append(palindromes)
                return
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    backtrack(j + 1, palindromes + [s[i:j + 1]])
            
        backtrack(0, [])

        return res
 
