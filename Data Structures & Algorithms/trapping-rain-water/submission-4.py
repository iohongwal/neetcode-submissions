class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        maxL = height[0]
        maxR = height[-1]

        L, R = 0, len(height) - 1

        area = 0

        while L < R:
            L_area = min(maxL, maxR) - height[L]
            if L_area > 0:
                area += L_area
            
            R_area = min(maxL, maxR) - height[R]
            if R_area > 0:
                area += R_area
            
            maxL = max(height[L], maxL)
            maxR = max(height[R], maxR)

            if maxL <= maxR:
                L += 1
            else:
                R -= 1

        return area


        