class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        new = intervals[0] #initiate the new interval

        for i in intervals[1:]:
            if i[0] <= new[1]:
                new[1] = max(i[1], new[1])
                new[0] = min(i[0], new[0])
            else:
                res.append(new)
                new = i
            
        res.append(new)

        return res
      