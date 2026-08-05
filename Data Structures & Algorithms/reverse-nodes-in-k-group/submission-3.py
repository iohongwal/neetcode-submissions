# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # time:O(n), space: O(1)   
        curr = head
        dummy = ListNode(0, head)
        prevGroup = dummy

        def helper(curr, k):
            #return the curr node when reach k
            while curr and k > 1:
                curr = curr.next
                k -= 1
            return curr

        while True:
            kthNode = helper(curr, k)
            #if reach end, break the loop
            if not kthNode:
                break
            nextGroup = kthNode.next #the next node after kth Node

            prev, curr = kthNode.next, prevGroup.next

            while curr != nextGroup:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            tmp = prevGroup.next
            prevGroup.next = kthNode
            prevGroup = tmp
            curr = nextGroup

        return dummy.next

        # time:O(n), space: O(k)        
        # curr = head
        # dummy = ListNode()
        # tail = dummy
        # stack = []
        # while curr:
        #     stack.append(curr)
        #     curr = curr.next

        #     if len(stack) == k:
        #         while stack:
        #             tail.next = stack.pop()
        #             tail = tail.next
        #         tail.next = curr

        # if stack:
        #     tail.next = stack[0]

        # return dummy.next