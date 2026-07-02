class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjHash = {c: [] for word in words for c in word}

        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            n, m = len(w1), len(w2)
            if n > m and w1[:m] == w2: 
                return ""
            for j in range(min(n, m)):
                c1, c2 = w1[j], w2[j]
                if c1 != c2:
                    adjHash[c1].append(c2)
                    break
        
        visited = set()
        visiting = set()
        topSort = []

        def dfs(c):

            if c in visited:
                return True
            
            if c in visiting:
                return False
            
            visiting.add(c)

            for c2 in adjHash[c]:
                if not dfs(c2):
                    return False

            visited.add(c)
            topSort.append(c)
            visiting.remove(c)

            return True

        for char in list(adjHash):
            if not dfs(char):
                return "" 
        topSort.reverse()
        return "".join(topSort)
                    
