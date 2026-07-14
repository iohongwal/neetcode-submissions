class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cows = len(heights), len(heights[0])
        neigbor = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        pacific = set()
        atlantic = set()

        def backtrack(r, c, height, visit):
            if (r < 0 or c < 0 or
                r >= rows or c >= cows or
                (r, c) in visit or
                heights[r][c] < height
            ):
                return

            visit.add((r, c))

            for n in neigbor:
                backtrack(r + n[0], c + n[1], heights[r][c], visit)

            
        for c in range(cows):
            backtrack(0, c, heights[0][c], pacific)
            backtrack(rows - 1, c, heights[rows - 1][c], atlantic)
        
        for r in range(rows):
            backtrack(r, 0, heights[r][0], pacific)
            backtrack(r, cows - 1, heights[r][cows - 1], atlantic)
        
        res = []

        for (r, c) in pacific:
            if (r, c) in atlantic:
                res.append([r,c])
        
        return res