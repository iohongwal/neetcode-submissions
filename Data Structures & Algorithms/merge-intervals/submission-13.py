class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        newInterval = intervals[0]
        for interval in intervals[1:]:
            if newInterval[1] >= interval[0]:
                newInterval[0] = min(interval[0],  newInterval[0])
                newInterval[1] = max(interval[1],  newInterval[1])
            else:
                res.append(newInterval)
                newInterval = interval
        res.append(newInterval)
        return res
