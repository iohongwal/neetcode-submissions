class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()
        intervals_heap = [] #interval, end time
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(intervals_heap, (r - l + 1, r))
                i += 1

            while intervals_heap and intervals_heap[0][1] < q:
                heapq.heappop(intervals_heap)
            
            res[q] = intervals_heap[0][0] if intervals_heap else -1



        return [res[q] for q in queries]