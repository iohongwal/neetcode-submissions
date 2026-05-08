class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return [-1]
        rightMax = -1
        for i in range(len(arr)-1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr