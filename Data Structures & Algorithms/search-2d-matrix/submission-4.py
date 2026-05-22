class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        l = 0
        r = rows * cols - 1 #flattened 2D to 1D
        while l <= r:
            mid = (l + r) // 2
            row = mid // cols
            col = mid % cols
            if target > matrix[row][col]:
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                return True

        return False
        