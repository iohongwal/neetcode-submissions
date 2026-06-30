class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        #define the hashmap as adacency list
        adjHash = collections.defaultdict(list)
        for i, [n1, n2] in enumerate(edges):
            adjHash[n1].append((n2, succProb[i]))
            adjHash[n2].append((n1, succProb[i]))
         
        #define a visited set to record the visited node
        visited = set()
        maxProb = 0
        #define a maxHeap for return largest succProb of that node
        maxHeap = [(-1.0, start_node)] #start from k with succProb 1

        #iterate each node 
        while maxHeap:
            prob1, node1 = heapq.heappop(maxHeap)
            
            #reach the end node
            if node1 == end_node:
                return -prob1

            if node1 in visited:
                continue
            
            visited.add(node1)
            maxProb = max(-maxProb, -prob1)
            
            #iterate all other node that connected to node1
            for node2, prob2 in adjHash[node1]:
                #check if the node(node2) is visited
                if node2 not in visited:
                    #the prob of start is -1.0 (keep it negative for the max heap)
                    heapq.heappush(maxHeap, ((prob2 * prob1), node2))

        return 0.0
            
