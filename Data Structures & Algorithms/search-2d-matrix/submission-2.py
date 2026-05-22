class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for vector in matrix:
            l, r = 0, len(vector) - 1
            if target > vector[r]:
                continue
            while l <= r:
                mid = (l + r) // 2
                if target > vector[mid]:
                    l = mid + 1
                elif target < vector[mid]:
                    r = mid - 1
                else:
                    return True

        return False
        