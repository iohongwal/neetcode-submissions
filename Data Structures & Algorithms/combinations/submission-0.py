class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, subset = [], []

        def backtrack(i):
            #Basecase
            #reach k integers in subset
            if len(subset) == k:
                res.append(subset.copy())
                return
            
            #Out of bounds handler
            if i > n:
                return
            
            #Don't Pick n
            backtrack(i + 1)

            #Pick n
            subset.append(i)
            backtrack(i + 1)
            #clear subset
            subset.pop()
        
        backtrack(1)

        return res