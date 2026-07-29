class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = (len(nums1) + len(nums2))
        half = n // 2
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 #left partition index of A
            j = half - i - 2 #left partition index of B

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")

            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                return (min(Bright, Aright) if (n % 2) 
                    else (max(Aleft, Bleft) + min(Bright, Aright))/2)
            
            elif Aleft > Bright:
                r = i - 1

            else: # Bright > Aleft
                l = i + 1
            





