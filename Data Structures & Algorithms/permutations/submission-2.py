class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, perm = [], []
        visited = [False] * len(nums)

        def backtrack():
            #Base Case:
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                perm.append(nums[i])
                visited[i] = True

                backtrack()

                perm.pop()
                visited[i] = False

        backtrack()
        return res
