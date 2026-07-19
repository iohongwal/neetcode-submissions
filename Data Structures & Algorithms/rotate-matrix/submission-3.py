class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        #Swipe the top x row with last x row
        for i in range(n//2):
            tmp = matrix[i]
            matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]
        
        #Transpose the martix - swipe the diagonal cells
        for i in range(n - 1):
            #iterate upper right concer only
            #because the lower left concer will be swiped by upper right concer
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]