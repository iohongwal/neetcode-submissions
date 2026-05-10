# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr: Optional[ListNode], prev: Optional[ListNode]):
            #default status
            #node = None means out of bounds
            if curr is None:
                return prev
            else:
                next = curr.next
                curr.next = prev
                prev = curr
            return reverse(next, prev)

        return reverse(head, None)