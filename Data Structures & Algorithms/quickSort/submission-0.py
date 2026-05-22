# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.qsortHelper(pairs, 0, len(pairs))

    def qsortHelper(self, arr: List[Pair], start, end):
        if end - start <= 1:
            return arr

        pivot = arr[end - 1].key
        left = start
        #iterate the arr and compare to pivot
        for i in range (start, end - 1):
            if arr[i].key < pivot:
                temp = arr[left]
                arr[left] = arr[i]
                arr[i] = temp
                left += 1
        #exchange the pviot
        temp = arr[end - 1]
        arr[end - 1] = arr[left]
        arr[left] = temp

        #recursion
        self.qsortHelper(arr, start, left)
        self.qsortHelper(arr, left + 1, end)

        return arr