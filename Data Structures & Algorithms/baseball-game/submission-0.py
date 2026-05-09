class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []
        result = 0
        for operator in operations:
            if operator == "+":
                temp = score_stack[-1] + score_stack[-2]
                score_stack.append(temp)
            elif operator == "D":
                temp = score_stack[-1] * 2
                score_stack.append(temp)
            elif operator == "C":
                score_stack.pop()
            else:
                score_stack.append(int(operator))
        while score_stack:
            result += score_stack.pop()
        return result