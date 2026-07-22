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
                if n not in row[i]:
                    row[i].add(n)
                else:
                    return False
                if n not in col[j]:
                    col[j].add(n)
                else:
                    return False
                if n not in square[(i//3, j//3)]:
                    square[(i//3, j/3)].add(n)
                else:
                    return False

        return True