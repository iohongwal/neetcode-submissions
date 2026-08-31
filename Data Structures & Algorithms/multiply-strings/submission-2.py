class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        
        def helper(num: str) -> int:
            numInt = 0
            for c in num:
                numInt *= 10
                numInt += ord(c) - ord("0")
            
            return numInt
        
        res = helper(num1)
        res *= helper(num2)

        return str(res)

