class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        L, R = 0, len(height) - 1
        maxL, maxR = height[L], height[R]
        area = 0

        while L < R:
            # We always process the side with the SMALLER maximum height.
            # This guarantees that water can be trapped safely up to this smaller max.
            if maxL < maxR:
                L += 1
                # Update the max height seen so far on the left
                maxL = max(maxL, height[L])
                # Calculate water at current L. 
                # (If height[L] is a new max, maxL - height[L] will just be 0!)
                area += maxL - height[L]
            else:
                R -= 1
                # Update the max height seen so far on the right
                maxR = max(maxR, height[R])
                # Calculate water at current R.
                area += maxR - height[R]

        return area