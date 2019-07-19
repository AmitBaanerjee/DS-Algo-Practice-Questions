# 965. Univalued Binary Tree
#
# A binary tree is univalued if every node in the tree has the same value.
#
# Return true if and only if the given tree is univalued.
#
# Example 1:
#
# Input: [1,1,1,1,1,null,1]
# Output: true
# Example 2:
#
# Input: [2,2,2,5,2]
# Output: false

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isUnivalTree(TreeNode root) {
        HashSet<Integer> hs=new HashSet<Integer>();
        Stack<TreeNode> s=new Stack<TreeNode>();
        s.push(root);
        while(!s.empty()){
            TreeNode current=s.pop();
            hs.add(current.val);
            if(current.left!=null){
                s.push(current.left);
            }
            if(current.right!=null){
                s.push(current.right);
            }
        }
        if (hs.size()>1){
            return false;
        }
        else{
            return true;
        }
    }
}
