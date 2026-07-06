class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #memorization
        cache = {}

        def backtrack(i, j):
            if i >= len(word1):
                #return num of insert operations
                return len(word2) - j
                
            if j >= len(word2):
                #return num of delet operations
                return len(word1) - i
            
            if (i, j) in cache:
                return cache[(i, j)]

            if word1[i] == word2[j]:
                return backtrack(i + 1, j + 1)

            cache[(i, j)] = 1 + min(
                # insert the character at the current index of word1
                backtrack(i, j + 1), 
                # delete the current character of word1
                backtrack(i + 1, j),
                # replace the character at index i
                backtrack(i + 1, j + 1)
                )

            return cache[(i, j)]
            
        
        return backtrack(0, 0)