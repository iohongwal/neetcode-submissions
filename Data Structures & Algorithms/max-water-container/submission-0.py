class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 
        L, R = 0, len(heights) - 1

        while L < R:
            area = (R - L) * min(heights[L], heights[R])
            max_area = max(area, max_area)

            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1

        return max_area