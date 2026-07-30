class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(":")", "{":"}", "[":"]"}
        
        for c in s:
            if c in mapping:
                stack.append(mapping[c])
                continue
            if stack and stack[-1] == c:
                stack.pop()
            else:
                return False
        
        return not stack
            
