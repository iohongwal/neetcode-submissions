class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, perm = [], []
        visited = [False] * len(nums)
        nums.sort()
        
        def backtrack():
            #Base Case:
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                # If this number is same as the one before it, AND the one 
                # before it is NOT currently in our permutation... SKIP IT!
                if i > 0 and nums[i - 1] == nums[i] and not visited[i - 1]:
                    continue

                perm.append(nums[i])
                visited[i] = True

                backtrack()

                perm.pop()
                visited[i] = False

        backtrack()
        return res
