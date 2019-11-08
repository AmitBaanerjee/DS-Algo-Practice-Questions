101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

   # Definition for a binary tree node.
   # class TreeNode:
   #     def __init__(self, x):
   #         self.val = x
   #         self.left = None
   #         self.right = None

   class Solution:
       def isSymmetric(self, root: TreeNode) -> bool:
           def helper(root_a,root_b):
               if root_a==None and root_b==None:
                   return True
               if root_a==None or root_b==None:
                   return False
               return root_a.val==root_b.val and helper(root_a.left,root_b.right) and helper(root_a.right,root_b.left)
           if root==None:
               return True
           else:
               return helper(root.left,root.right)
