class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = stoneSum // 2

        dp = {}

        def backtrack(i, total):
            #Base case
            if i == len(stones) or total >= target:
                return abs(total - (stoneSum - total))
            
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = min(
                    backtrack(i + 1, total), 
                    backtrack(i + 1, total + stones[i]), 
                    )
            
            return dp[(i, total)]
            
        return backtrack(0, 0)

        