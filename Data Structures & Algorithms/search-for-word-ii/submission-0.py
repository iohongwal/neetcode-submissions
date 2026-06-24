class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = None

    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = TrieNode()
        # add all words into trie struct
        for word in words:
            trie.insert(word)

        ROW, COL = len(board), len(board[0])

        # res save the word res while visited save the visited node result
        res, visited = [], set() 

        
        def dfs(r, c, node):

            if (r < 0 or c < 0 or r == ROW or c == COL or # check if r or c out of bound
                (r, c) in visited or board[r][c] not in node.children
                ):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            
            if node.word:
                res.append(node.word)
                node.word = None #only find the word once

            dfs(r - 1, c, node)
            dfs(r + 1, c, node)
            dfs(r, c - 1, node)
            dfs(r, c + 1, node)

            visited.remove((r, c))

        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, trie)
        
        return res
        
        
        