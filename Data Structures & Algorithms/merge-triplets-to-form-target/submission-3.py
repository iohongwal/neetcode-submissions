class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        new = [0] * 3
        for i in range(len(triplets)):
            """
            compare triples and target, if the triples > target, skip current triples
            """
            if (
                triplets[i][0] > target[0] or
                triplets[i][1] > target[1] or
                triplets[i][2] > target[2]
            ):
                continue
            
            for j in range(3):
                new[j] = max(new[j], triplets[i][j]) 
                    

        return new == target

