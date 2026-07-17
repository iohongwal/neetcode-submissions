class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, n in enumerate(intervals):
            #Base case:
            if newInterval[1] < n[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif n[1] < newInterval[0]:
                res.append(n)
            else:
                newInterval[0] = min(n[0], newInterval[0])
                newInterval[1] = max(n[1], newInterval[1])
        
        res.append(newInterval)
        return res

        #my solutation O(n)
        # res = []
        # for i, n in enumerate(intervals):
        #     if newInterval[0] <= n[1]:
        #         newInterval[0] = min(n[0], newInterval[0])
        #     if n[0] <= newInterval[1]:
        #         newInterval[1] = max(n[1], newInterval[1])

        #     if not(newInterval[0] <= n[0] <= newInterval[1]):
        #         if newInterval[0] < n[0] and newInterval[1] < n[1]:
        #             res.append(newInterval)
        #             return res + intervals[i:]
        #         res.append(n)
        # res.append(newInterval)
        # return res
            