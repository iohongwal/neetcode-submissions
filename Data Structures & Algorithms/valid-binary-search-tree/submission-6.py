# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, boundary):
            if not root:
                return True
            
            if not (boundary[0] < root.val < boundary[1]):
                return False

            return dfs(root.left, [boundary[0], root.val]) and dfs(root.right, [root.val, boundary[1]])
        
        return dfs(root, [float('-inf'), float('inf')])