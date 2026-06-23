# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxSum = 0
        slowNode, fastNode = head, head
        prevNode = None
        while fastNode and fastNode.next:
            fastNode = fastNode.next.next
            curNode = slowNode 
            slowNode = slowNode.next
            curNode.next = prevNode
            prevNode = curNode
        
        while slowNode and prevNode:
            twinSum = slowNode.val + prevNode.val
            maxSum = max(maxSum, twinSum)
            slowNode = slowNode.next
            prevNode = prevNode.next

        return maxSum