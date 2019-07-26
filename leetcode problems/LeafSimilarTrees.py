# 872. Leaf-Similar Trees
#
# Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
#
#               3
#             /   \
#            5     1
#           /\     /\
#          6  2   9  8
#         /\
#        7  4
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

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
    public List<Integer> genTreeList(TreeNode root){
        Stack<TreeNode> st= new Stack<TreeNode>();
        List<Integer> leaves=new ArrayList<Integer>();
        st.push(root);
        while(!st.empty()){
            TreeNode n=st.pop();
            if(n.left==null && n.right==null){
                leaves.add(n.val);
            }
            else{
                if(n.left!=null){
                    st.push(n.left);
                }
                if(n.right!=null){
                    st.push(n.right);
                }
            }
        }
        return leaves;
    }
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> l1=genTreeList(root1);
        List<Integer> l2=genTreeList(root2);
        return l1.equals(l2);
    }
}
