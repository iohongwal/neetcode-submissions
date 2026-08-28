class Solution:
    def checkValidString(self, s: str) -> bool:
        left_max_num = 0
        left_min_num = 0

        for c in s:
            if c == "(":
                left_max_num += 1
                left_min_num += 1
            elif c == ')':
                left_max_num -= 1
                left_min_num -= 1
            else:
                left_max_num += 1 
                left_min_num -= 1
            
            if left_max_num < 0:
                return False
            if left_min_num < 0:
                left_min_num = 0
            
        return left_min_num == 0