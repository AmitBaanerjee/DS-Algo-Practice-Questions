897. Increasing Order Search Tree

Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9

 /**
  * Definition for a binary tree node.
  * public class TreeNode {
  *     int val;
  *     TreeNode left;
  *     TreeNode right;
  *     TreeNode(int x) {
         val = x;
         }
  * }
  */
 class Solution {
     public void inorder(TreeNode node, List<Integer> l){
         if (node==null) return;
         inorder(node.left,l);
         l.add(node.val);
         inorder(node.right,l);
     }
     public TreeNode increasingBST(TreeNode root) {
         List<Integer> l=new ArrayList<Integer>();
         inorder(root,l);
         TreeNode output=new TreeNode(0);
         TreeNode current=output;
         for(int i:l){
             current.right=new TreeNode(i);
             current=current.right;
         }
         return output.right;
     }
 }
