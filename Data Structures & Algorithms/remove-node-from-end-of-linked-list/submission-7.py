# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #fast and slow pointer
        dummy = ListNode(0, head)
        fast, slow  = dummy, dummy
        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

        #reverse apporach

        # def reverseList(curr, prev):
        #     if not curr:
        #         return prev
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr
        #     return reverseList(next, prev)

        # #Recerse the given linkList
        # curr = head
        # reverseCurr = reverseList(curr, None)

        # curr = reverseCurr
        # prev = None
        # while n > 1 and curr:
        #     prev = curr
        #     curr = curr.next
        #     n -= 1
        
        # if prev:
        #     prev.next = curr.next if curr else None
        # else:
        #     reverseCurr = curr.next
        
        # res = reverseList(reverseCurr, None)

        # return res