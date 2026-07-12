# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        treeStr = []
        def dfs(root):
            if not root:
                treeStr.append("N")
                return
            treeStr.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ",".join(treeStr)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        dataSplit = data.split(",")
        self.idx = 0
        def dfs():
            if dataSplit[self.idx] == "N":
                self.idx += 1
                return None
            if self.idx >= len(dataSplit):
                return node

            node = TreeNode(int(dataSplit[self.idx]))
            self.idx += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


