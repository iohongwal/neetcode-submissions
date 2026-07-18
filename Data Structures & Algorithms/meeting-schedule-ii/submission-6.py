"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        count = 0
        s = [interval.start for interval in intervals]
        e = [interval.end for interval in intervals]
        s.sort()
        e.sort()
        res_count = 0
        i, j = 0, 0
        while i < len(s) and j < len(e):
            if i < len(s):
                if s[i] < e[j]:
                    count += 1
                    i += 1
                else: 
                    count -= 1
                    j += 1
                res_count = max(count, res_count)

        return res_count