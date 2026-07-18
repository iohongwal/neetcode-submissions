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
        
        # The "Sweep Line" approach: 
        # We don't care about specific interval pairings anymore. 
        # We just want a chronological timeline of "starts" (+1 room) and "ends" (-1 room).
        count = 0
        
        # Separate and sort the start times and end times independently
        s = [interval.start for interval in intervals]
        e = [interval.end for interval in intervals]
        s.sort()
        e.sort()
        
        res_count = 0
        i, j = 0, 0
        
        # Walk through the timeline chronologically
        while i < len(s) and j < len(e):
            if i < len(s):
                # If the next chronological event is a meeting starting...
                if s[i] < e[j]:
                    count += 1      # We need an additional room
                    i += 1          # Move the start pointer forward
                
                # If the next chronological event is a meeting ending...
                else: 
                    count -= 1      # A room just freed up!
                    j += 1          # Move the end pointer forward
                
                # Record the maximum number of simultaneous rooms ever needed
                res_count = max(count, res_count)

        return res_count