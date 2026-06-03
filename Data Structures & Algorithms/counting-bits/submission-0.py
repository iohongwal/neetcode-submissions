class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def count1Bits(n:int) -> int:
            res = 0
            while n:
                n &= n - 1
                res += 1
            return res
        
        res = []
        
        for i in range(0, n + 1, 1):
            res.append(count1Bits(i))
        
        return res