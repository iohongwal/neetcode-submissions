class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1]]
        lastRow = [1]
        for n in range(2, numRows + 1):
            newRow = [0] * n
            for i in range(n):
                newRow[i] = lastRow[i - 1] if i > 0 else 0
                newRow[i] += lastRow[i] if i < len(lastRow) else 0  
            res.append(newRow)
            lastRow = newRow
        
        return res

