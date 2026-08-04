# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tens = 0
        dummpy = ListNode()
        curL1, curL2 = l1, l2
        cur = dummpy
        while curL1 or curL2 or tens > 0:
            newVal = 0
            if curL1:
                newVal += curL1.val
                curL1 = curL1.next
            if curL2:
                newVal += curL2.val
                curL2 = curL2.next
            
            newVal += tens
            
            tens = newVal // 10
            newVal %= 10

            newNode = ListNode(newVal)
            cur.next = newNode
            cur = cur.next
        
        return dummpy.next
