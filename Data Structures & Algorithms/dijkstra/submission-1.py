class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        #Initial Adjacency list (hashmap) and put all edges into it
        adj = {}
        for i in range(0, n):
            adj[i] = []
        for u, v, w in edges:
            adj[u].append((v, w))

        shortest = {}
        minHeap = [(0, src)]

        while minHeap:
            #get the closest node from minHeap
            w1, n1 = heapq.heappop(minHeap)
            #check if the node in the shortest hashmap
            #if yes, jump to next loop
            if n1 in shortest:
                continue
            #push the closest node into the shortest hashmap
            shortest[n1] = w1

            #iterate the Adjacency list of the node
            #check if the next node in the shortest
            #if not, push to shortest hashmap
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest