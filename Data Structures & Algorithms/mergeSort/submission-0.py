# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs))

    def mergeSortHelper(self, arr, start, end):
        if end - start <= 1:
            return arr # Base case: segment has 0 or 1 element
        mid = (start + end) // 2
        self.mergeSortHelper(arr, start, mid)
        self.mergeSortHelper(arr, mid, end)
        self.merge(arr, start, mid , end)

        return arr

    def merge(self, arr, start, mid , end):
        i, j, k = 0, 0, 0
        L = arr[start: mid]
        R = arr[mid: end]
        i, j = 0, 0
        k = start
        # Merge the two sorted halfs
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

