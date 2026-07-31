class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthese = {"(":")", "{":"}", "[":"]"}

        for c in s:
            if c in parenthese:
                stack.append(parenthese[c])
                continue
            if stack and c == stack[-1]:
                stack.pop()
            else:
                return False
                
        
        return not stack
        