class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            idx = i
            while stack and heights[i] < stack[-1][1]:
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))

            stack.append((idx, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
        
