class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {} 

        for task in tasks:
            count[task] = 1 + count.get(task, 0)
        
        #maxHeap
        freqHeap = []

        for task, count in count.items():
            if count > 0:
                heapq.heappush(freqHeap, -count)
        
        time = 0
        queue = deque()
        while freqHeap or queue:
            if freqHeap:
                count = heapq.heappop(freqHeap) + 1
                if count < 0:
                    queue.append((count, time + n))
            if queue and queue[0][1] == time:
                count, _ = queue.popleft()
                heapq.heappush(freqHeap, count)
            
            time += 1
        
        return time
            

