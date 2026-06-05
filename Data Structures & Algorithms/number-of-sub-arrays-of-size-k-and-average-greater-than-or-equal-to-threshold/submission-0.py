class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0
        L = 0
        curSum = 0

        for R in range(len(arr)):
            curSum += arr[R]
            # windows check
            if R - L + 1 == k:
                if curSum >= threshold * k:
                    counter += 1
                
                curSum -= arr[L]
                L += 1

        return counter
