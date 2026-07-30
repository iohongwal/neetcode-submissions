class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet = set()

        def helper(n: int) -> bool:
            if n == 1:
                return True

            if n in hashSet:
                return False

            hashSet.add(n)

            total_sum = 0
            while n > 0:
                digit = n % 10
                total_sum += digit * digit
                n = n // 10

            return helper(total_sum)
        
        return helper(n)

            
            

            
                