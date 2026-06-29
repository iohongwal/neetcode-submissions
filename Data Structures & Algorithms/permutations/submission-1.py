class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(i):
            #Base case
            if i >= len(nums):
                return [[]]

            newPerm = []
            perm = backtrack(i + 1)
            for p in perm:
                for j in range(len(p) + 1):
                     pCopy = p.copy()
                     pCopy.insert(j, nums[i])
                     newPerm.append(pCopy)
            
            return newPerm

        return backtrack(0)
                