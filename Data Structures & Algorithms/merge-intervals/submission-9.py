class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        new = intervals[0]
        for i in intervals:
            if i[0] <= new[1]:
                new[0] = min(new[0], i[0])
                new[1] = max(new[1], i[1])
            else:
                res.append(new)
                new = i
        res.append(new)
        return res
        