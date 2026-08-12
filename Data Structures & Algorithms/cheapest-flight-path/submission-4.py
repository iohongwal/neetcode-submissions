class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjHeap = collections.defaultdict(list) #org: (price, des)

        for org, des, price in flights:
            heapq.heappush(adjHeap[org], (price, des))

        queue = deque([(0, src)])
        stops = 0
        dist = [float("inf")] * n
        while queue and stops <= k + 1:
            for _ in range(len(queue)):
                curPrice, curStop = queue.popleft()
                if curPrice >= dist[curStop]:
                    continue
                dist[curStop] = curPrice
                for price, neigbour in adjHeap[curStop]:
                    queue.append((curPrice + price, neigbour))
            
            stops += 1

        return dist[dst] if dist[dst] != float("inf") else -1