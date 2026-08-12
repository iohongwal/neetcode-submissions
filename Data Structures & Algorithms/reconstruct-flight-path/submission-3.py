class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = collections.defaultdict(list)

        for org, des in tickets:
            heapq.heappush(adjList[org], des)
        
        res = []
        flown = set()
        def dfs(org):
            while adjList[org]:
                des = heapq.heappop(adjList[org])
                dfs(des)
            res.append(org)

        dfs("JFK")
        return res[::-1]
        

