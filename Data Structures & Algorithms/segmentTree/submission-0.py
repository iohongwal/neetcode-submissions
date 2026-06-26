class TreeNode():

    def __init__(self, total, L, R):
        self.sum = total
        self.L = L
        self.R = R
        self.left = None
        self.right = None

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums: List[int], L, R):
        if L == R:
            return TreeNode(nums[L], L, R)
        
        mid = (L + R) // 2
        root = TreeNode(0, L, R)
        root.left = self.build(nums, L, mid)
        root.right = self.build(nums, mid + 1, R)
        root.sum = root.left.sum + root.right.sum

        return root
    
    def update(self, index: int, val: int) -> None:
        def update_helper(root: TreeNode, index: int, val: int):
            L , R = root.L, root.R

            if L == R == index:
                root.sum = val
                return

            mid = (L + R) // 2

            if index > mid:
                update_helper(root.right, index, val)
            else:
                update_helper(root.left, index, val)
            
            root.sum = root.left.sum + root.right.sum

        update_helper(self.root, index, val)
        
    def query(self, L: int, R: int) -> int:

        def query_helper(root: TreeNode, L, R):
            if root.L > R or L > root.R:
                return 0
            if L <= root.L and root.R <= R:
                return root.sum

            return (query_helper(root.left, L, R) + 
                query_helper(root.right, L, R))

        return query_helper(self.root, L, R)
