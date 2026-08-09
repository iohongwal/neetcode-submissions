class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        neigbhor = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows, cols = len(grid), len(grid[0])
        quene = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    quene.append((r, c))

        layer = 0
        while quene:
            for _ in range(len(quene)):
                r, c = quene.popleft()
                for nr, nc in neigbhor:
                    newR, newC = r + nr, c + nc
                    if ( 
                        0 <= newR < rows and 
                        0 <= newC < cols and
                        grid[newR][newC] == 2147483647
                    ):
                        quene.append((newR, newC))
                        grid[newR][newC] = grid[r][c] + 1
                
                grid[r][c] = min(layer, grid[r][c])

            layer += 1
        
        