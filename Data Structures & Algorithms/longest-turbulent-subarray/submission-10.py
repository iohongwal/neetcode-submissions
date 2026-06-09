class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if not arr: 
            return 0
        if len(arr) < 2:
            return len(arr)
        length = 0
        L = 0
        greatSign = arr[0] > arr[1]
        for R in range(1 ,len(arr)):

            if arr[R] == arr[R - 1]:
                L = R

            elif (greatSign and arr[R] > arr[R - 1] or 
                not greatSign and arr[R] < arr[R - 1]):
                L = R - 1
            
            greatSign = arr[R] > arr[R - 1]

            length = max(length, R - L + 1)

        return length