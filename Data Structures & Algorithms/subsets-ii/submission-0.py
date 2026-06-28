class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        #Sort the nums for easier handle the duplicate
        nums = sorted(nums) 
        def backtrack(i):
            #check if out of bound.
            #if out of bound, append the current subset to result
            if i >= len(nums):
                res.append(subset.copy())
                return

            #Pick the num
            subset.append(nums[i])
            backtrack(i + 1)
            #Clear the subset
            subset.pop()

            #Don't pick
            #Check duplicate num and skip all the duplication
            while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

            
        
        backtrack(0)
        return res