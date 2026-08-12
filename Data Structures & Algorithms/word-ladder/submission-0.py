class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjList = collections.defaultdict(list)
        #Form the adjList use the word of wordList
        #create all possible edge for each word with wilcard combination
        wordLen = len(beginWord)
        visited = {beginWord}  
        queue = deque([beginWord])
        layer = 1

        for i in range(len(wordList)):
            for j in range(wordLen):
                key = wordList[i][:j] + "*" + wordList[i][j + 1:]
                adjList[key].append(wordList[i])

        while queue:

            for _ in range(len(queue)):
                curWord  = queue.popleft()
                if curWord == endWord:
                    return layer
                for i in range(wordLen):
                    pattern  = curWord[:i] + "*" + curWord[i+1:]
                    for neighbor  in adjList[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)

            layer += 1

        return 0

    
        
                


