class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            if (token != "+" and 
                token != "-" and
                token != "*" and
                token != "/"):
                stack.append(int(token))
                continue

            right = stack.pop()
            if stack:
                left = stack.pop()
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))

        return stack[-1]