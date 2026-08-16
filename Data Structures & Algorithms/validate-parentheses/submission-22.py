class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {"(":")", "[":"]", "{":"}"}
        for c in s:
            if c in parentheses:
                stack.append(parentheses[c])
            elif stack and c == stack[-1]:
                stack.pop()
            else:
                return False
        
        return False if stack else True