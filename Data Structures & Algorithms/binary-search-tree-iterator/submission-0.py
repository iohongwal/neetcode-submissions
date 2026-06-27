# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.inorder = deque()

        cur = self.root
        stack = []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                self.inorder.append(cur)
                cur = cur.right

    def next(self) -> int:

        return self.inorder.popleft().val

    def hasNext(self) -> bool:
        if self.inorder:
            return True
        return False

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()