class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        new = [0] * 3
        for a, b, c in triplets:
            """
            compare triples and target, if the triples > target, skip current triples
            """
            if (
                a <= target[0] and
                b <= target[1] and
                c <= target[2]
            ):   
                new[0] = max(new[0], a) 
                new[1] = max(new[1], b)  
                new[2] = max(new[2], c) 
                    

        return new == target

