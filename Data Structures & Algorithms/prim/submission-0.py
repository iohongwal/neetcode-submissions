class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        #Initiate a Adjacency Hashmap to store the edges
        adjHash = collections.defaultdict(list)
        for u, v, w in edges:
            adjHash[u].append([v, w])
            adjHash[v].append([u, w])
        
        visited = set()
        minHeap = [(0, 0)] #(weigth, node)
        min_weight = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            
            if n1 in visited:
                continue
            
            visited.add(n1)
            min_weight += w1

            if len(visited) == n:
                return min_weight
            
            for n2, w2 in adjHash[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, [w2, n2])

        return -1




        