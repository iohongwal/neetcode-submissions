class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = []
        if dst not in self.adjList:
            self.adjList[dst] = []
        self.adjList[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adjList and dst in self.adjList[src]:
            self.adjList[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        if not self.adjList[src]:
            return False

        length = 0
        visited = set()
        queue = deque()

        queue.append(src)
        visited.add(src)

        while queue:
            for _ in range(len(queue)):
                curNode = queue.popleft()
                if curNode == dst:
                    return True

                for nextNode in self.adjList[curNode]:
                    if nextNode not in visited:
                        queue.append(nextNode)
                        visited.add(nextNode)
            
    
        return False
