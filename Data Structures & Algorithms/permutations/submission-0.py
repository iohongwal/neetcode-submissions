class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for n in nums:
            nextPerm = []
            for p in permutations:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    nextPerm.append(pCopy)
            permutations = nextPerm

        return permutations
