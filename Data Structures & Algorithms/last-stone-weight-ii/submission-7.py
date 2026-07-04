class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = stoneSum // 2

        # dp[j] will be True if we can create a pile of exact weight 'j'
        dp = [False] * (target + 1)
        dp[0] = True # We can always make a pile of weight 0

        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = dp[j] or dp[j - stone]

        max_pile_1 = 0
        for j in range(target, -1, -1):
            if dp[j]:
                max_pile_1 = j
                break
        
        pile_2 = stoneSum - max_pile_1
        return pile_2 - max_pile_1

        #DP Buttom-up
        n = len(stones)
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for t in range(target + 1):
                if t >= stones[i - 1]:
                    dp[i][t] = max(dp[i - 1][t], dp[i - 1][t - stones[i - 1]] + stones[i - 1])
                else:
                    dp[i][t] = dp[i - 1][t]
        return stoneSum - 2 * dp[n][target]


        # #DP (Top-Down)
        # dp = {}
        # def backtrack(i, total):
        #     #Base case
        #     if i == len(stones) or total >= target:
        #         return abs(total - (stoneSum - total))
            
        #     if (i, total) in dp:
        #         return dp[(i, total)]

        #     dp[(i, total)] = min(
        #             backtrack(i + 1, total), 
        #             backtrack(i + 1, total + stones[i]), 
        #             )
            
        #     return dp[(i, total)]
            
        # return backtrack(0, 0)

        # #Recursion

        # def backtrack(i, total):
        #     #Base case
        #     if i == len(stones) or total >= target:
        #         return abs(total - (stoneSum - total))
            
        #     return min(
        #             backtrack(i + 1, total), 
        #             backtrack(i + 1, total + stones[i]), 
        #             )
            
        # return backtrack(0, 0)

        