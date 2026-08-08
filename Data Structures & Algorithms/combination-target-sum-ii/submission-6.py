class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, target, combinations):
            if target == 0:
                res.append(combinations)
                return
            if i >= len(candidates) or target < 0:
                return

            #Skip all identical elements to avoid duplicates
            next_i = i + 1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1
            
            #Skip
            backtrack(next_i, target, combinations)
            #Pick
            backtrack(i + 1, target - candidates[i], combinations + [candidates[i]])


        backtrack(0, target, [])
        return res

