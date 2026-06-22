class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW, COL = len(matrix), len(matrix[0])
        self.matrix_sum = [[0] * (COL + 1) for r in range(ROW + 1)]
        for r in range(ROW):
            prefix_sum = 0
            for c in range(COL):
                #Update the running total for the current row
                prefix_sum += matrix[r][c]
                #Grab the total area of the rectangle sitting directly above us
                above_sum = self.matrix_sum[r][c + 1]
                #Combine them to store the absolute total area from (0,0) down to (r,c)
                self.matrix_sum[r + 1][c + 1] = prefix_sum + above_sum
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Shift all coordinates by +1 to align with our padded matrix_sum
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        BottomRight = self.matrix_sum[r2][c2] # Total area down to bottom-right
        LeftBox = self.matrix_sum[r2][c1 - 1] # the left bounding box
        TopBox = self.matrix_sum[r1 - 1][c2] # the top bounding box
        TopLeftOverlap = self.matrix_sum[r1 - 1][c1 - 1] # the overlapping top-left corner
        
        # Apply the Inclusion-Exclusion Principle:
        # Start with the massive rectangle up to the bottom-right corner.
        # Chop off the unwanted area above it and to the left of it.
        # Add back the top-left corner because it just got subtracted twice!
        return BottomRight - LeftBox - TopBox + TopLeftOverlap


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)