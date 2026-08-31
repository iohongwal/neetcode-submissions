class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if x == 0:
            return 0

        if n < 0:
            x = 1/x
            n = -n

        def helper(x, n):
            if n == 0:
                return 1

            half = helper(x, n // 2)
            
            if n % 2 == 0:
                return half * half
            
            return x * half * half
        
        return helper(x, n)
                