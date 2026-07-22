class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                n = board[i][j]
                if (n in row[i] or 
                    n in col[j] or
                    n in square[(i//3, j//3)]):
                    return False

     
                row[i].add(n)
                col[j].add(n)
                square[(i//3, j/3)].add(n)

        return True