class Solution:
    def solve(self, board: List[List[str]]) -> None:
        neigbhour = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] != "O"
            ):
                return

            board[r][c] = "S"
            
            for (nr, nc) in neigbhour:
                newR, newC = (r + nr), (c + nc)
                dfs(newR, newC)


        for r in range(rows):
                dfs(r, 0)
                dfs(r, cols - 1)
        
        for c in range(cols):
                dfs(0, c)
                dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "S":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"     
        

            

