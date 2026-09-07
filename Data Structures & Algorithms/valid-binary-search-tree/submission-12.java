/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isValidBST(TreeNode root) {
        return isBST(root, null, null);
    }

    boolean isBST(TreeNode root, Integer left_bound, Integer right_bound){
        if (root == null) return true;

        if (right_bound != null && root.val >= right_bound) return false;

        if (left_bound != null && root.val <= left_bound) return false; 

        return isBST(root.left, left_bound, root.val) && isBST(root.right, root.val, right_bound);
        
    }
}
