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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) return false;

        //Check if the current tree is same tree
        if (isSametree(root, subRoot)) return true;

        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    boolean isSametree(TreeNode root1, TreeNode root2){
        //both root1 and root2 reach to end
        if (root1 == null && root2 == null) return true;
        
        if (root1 == null || root2 == null || root1.val != root2.val) return false;

        return isSametree(root1.left, root2.left) && isSametree(root1.right, root2.right);
    }
    
}
