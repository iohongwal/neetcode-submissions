class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}
        return self.backtrack(0, profit, weight, capacity, memo)
        
    def backtrack(self, i, profit, weight, capacity, memo):
        #Basecase
        if i == len(profit):
            return 0
        
        state = (i, capacity)
        if state in memo:
            return memo[state]
        
        #Skip current item
        maxProfit = self.backtrack(i + 1, profit, weight, capacity, memo)

        #Take current item
        newCapacity = capacity - weight[i]
        if newCapacity >= 0:
            curProfit = profit[i] + self.backtrack(i + 1, profit, weight, newCapacity, memo)
            maxProfit = max(maxProfit, curProfit)
        
        memo[state] = maxProfit
        return maxProfit