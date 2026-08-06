class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) 

        #maxHeap
        freqHeap = [-cnt for cnt in count.values()]
        heapq.heapify(freqHeap)

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
            

