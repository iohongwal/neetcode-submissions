class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if prev[1] <= intervals[i][0]:
                prev = intervals[i]
            else:
                res += 1
                prev[1] = min(intervals[i][1], prev[1])

        return res