class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort()
        res = []
        new = intervals[0]
        for i in range(1, len(intervals)):
            if new[1] < intervals[i][0]:
                res.append(new)
                new = intervals[i]
            elif intervals[i][1] < new[0]:
                res.append(intervals[i])
            else:
                new = [
                    min(new[0], intervals[i][0]),
                    max(new[1], intervals[i][1]),
                ]
        
        res.append(new)
        return res

