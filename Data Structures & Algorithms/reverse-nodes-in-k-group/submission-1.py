# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        curr = head

        dummy = ListNode(0)
        tail = dummy
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next

            if len(stack) == k:
                while stack:
                    tail.next = stack.pop()
                    tail = tail.next
                tail.next = curr

        if stack:
            tail.next = stack[0]

        return dummy.next