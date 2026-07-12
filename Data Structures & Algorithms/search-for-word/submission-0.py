class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.res = ""
        visited = set()

        def backtrack(i, j, k):
            if k >= len(word):
                return True

            if (i < 0 or j < 0 or
                i >= len(board) or j >= len(board[0]) or
                board[i][j] != word[k] or
                (i, j) in visited):
                return False

            visited.add((i,j))

            res = False
            for n in neighbors:
                res = res or backtrack(i + n[0], j + n[1], k + 1)

            visited.remove((i,j))
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, 0):
                    return True

        return False
            
            