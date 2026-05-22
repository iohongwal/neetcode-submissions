# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def postorder(root) -> [bool, int]:
            if not root:
                return [True, 0]
            L = postorder(root.left)
            R = postorder(root.right)
            balance = L[0] and R[0] and abs(L[1] - R[1]) < 2 
            return [balance, 1 + max(L[1], R[1])]

        return postorder(root)[0]