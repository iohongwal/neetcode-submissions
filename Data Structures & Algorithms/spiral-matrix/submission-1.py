class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        res = []
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        while top <= bottom and left <= right:

            #iterate top x row
            for i in range(left, right + 1):
                res.append(matrix[top][i])

            top += 1
            #iterate right x colunm
            for i in range(top, bottom + 1):
                res.append(matrix[i][right]) 
            
            right -= 1 

            if top > bottom or left > right:
                break

            #iterate bottom x row
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            
            bottom -= 1

            #iterate left x colunm
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])

            left += 1

        return res