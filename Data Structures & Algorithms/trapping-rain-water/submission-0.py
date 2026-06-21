class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        maxL = [0] * n
        maxR = [0] * n
        area = 0

        #find the max height in L side
        current_max = 0
        for i in range(n):
            current_max = max(current_max, height[i])
            maxL[i] = current_max
        #find the max height in R side    
        current_max = 0
        for i in range(n -1, -1, -1):
            current_max = max(current_max, height[i])
            maxR[i] = current_max
        
        for i in range(n):
            area += min(maxL[i], maxR[i]) - height[i]

        return area


        