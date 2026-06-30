class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #define the hashmap as adacency list
        adj = {}
        #Add node 1 to n into adj
        for i in range(1, n + 1):
            adj[i] = []
        #construct the adjacency list
        for ui, vi, ti in times: 
            adj[ui].append((vi, ti))
        
        #define a visited set to record the visited node
        visited = set()
        maxTime = 0
        #define a minHeap for return min time of that node
        minHeap = [(0, k)] #start from k with it k to k distance 0

        #iterate each node 
        while minHeap:
            t1, u1 = heapq.heappop(minHeap)
            #check if the node(u1) is visited
            if u1 in visited:
                continue

            #push the min time node
            visited.add(u1)
            maxTime = max(maxTime, t1)
            
            #iterate all other node that connected to u1
            for u2, t2 in adj[u1]:
                #check if the node(u2) is visited
                if u2 not in visited:
                #push the total time and target node to minHeap
                    heapq.heappush(minHeap, ((t1 + t2), u2))

        return maxTime if len(visited) == n else -1
        
        
         


