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
        
        #define a minimum_time hashmap to store the min time of each node
        minimum_time = {}
        #define a minHeap for return min time of that node
        minHeap = [(0, k)] #start from k with it k to k distance 0

        #iterate each node 
        while minHeap:
            t1, u1 = heapq.heappop(minHeap)
            #check if the node(u1) in the minimum_time
            #if yes, jump to next loop as the minimum_time path found
            if u1 in minimum_time:
                continue

            #push the min time node
            minimum_time[u1] = t1
            
            #iterate all other node that connected to u1
            for u2, t2 in adj[u1]:
                #check if the min time path from u1 to u2 is found
                if u2 not in minimum_time:
                #push the total time and target node to minHeap
                    heapq.heappush(minHeap, ((t1 + t2), u2))
        res = 0
        for i in range(1, n + 1):
            #check if the node is reachable
            #if the node is unreachable, it will not in the minimum_time
            #then mark its time is -1
            if i not in minimum_time:
                return -1
            else:
                res = max(res, minimum_time[i])
        
        return res
        
        
         


