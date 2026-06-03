class Solution:
    def hammingWeight(self, n: int) -> int:
        
        counter = 0
        while n:
            counter += n % 2
            n = n >> 1
        return counter