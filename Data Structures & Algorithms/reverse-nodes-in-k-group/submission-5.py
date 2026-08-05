# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #1->2 => 2->1
        def reverseNode(curr, prev):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            return curr, prev
        
        #1->2->3, k = 3 => return node of 3
        def findKth(curr, k):
            while curr and k > 1:
                curr = curr.next
                k -= 1
            
            return curr

        dummy = ListNode(0, head)
        prev_group_head = dummy
        curr = head

        while True:
            #the kTh node is the prev_group_end
            prev_group_end = findKth(curr, k)
            #if the kTh node is None, end the iteration
            if not prev_group_end:
                break
            
            #1->2->3->4, k = 3
            #new_group_head is node 4
            #let 1 and 4 as curr and prev
            #then 2->3->1->4
            new_group_head = prev_group_end.next
            prev, curr = prev_group_end.next, prev_group_head.next


            while curr != new_group_head:
                curr, prev = reverseNode(curr, prev)
            
            #reassign prev_group
            # 3->2->1->4->5 
            # 
            # set 3 as new prev_group_head.next
            # reset prev_group_head as node of 4
        
            tmp = prev_group_head.next
            prev_group_head.next = prev_group_end
            prev_group_head = tmp
            curr = new_group_head
        
        return dummy.next
            
