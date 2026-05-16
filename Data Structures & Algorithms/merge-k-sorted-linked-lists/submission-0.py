# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) < 1:
            return None
        minheap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minheap, (node.val, i, node))
        
        Dummy = ListNode()
        curr = Dummy

        while minheap:
            val, i, node = heapq.heappop(minheap)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(minheap, (node.val, i, node))
        
        return Dummy.next
