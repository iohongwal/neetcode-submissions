class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, perm = [], []
        numsHash = {n : 0 for n in nums}
        for n in nums:
            numsHash[n] += 1

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in numsHash:
                if numsHash[n] > 0:
                    perm.append(n)
                    numsHash[n] -= 1

                    backtrack()
                    numsHash[n] += 1
                    perm.pop()
        backtrack()
        return res
