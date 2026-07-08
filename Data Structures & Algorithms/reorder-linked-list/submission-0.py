# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head

        #find the half node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        L = head
        R = slow.next
        slow.next = None
        prev_R = None

        #Reverse R half
        while R:
            next = R.next
            R.next = prev_R
            prev_R = R
            R = next

        # R is None after reverse the R half link list
        # Retrieve R from prev_R
        R = prev_R 

        #Reorder
        while L and R:
            tempL = L.next
            tempR = R.next
            L.next = R
            R.next = tempL
            L = tempL
            R = tempR
            