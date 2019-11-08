872. Leaf-Similar Trees

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        if root1==None or root2==None:
            return False
        if root1==None and root2==None:
            return True
        def helper(root,list1):
            if root==None:
                return
            if root.left==None and root.right==None:
                list1.append(root.val)
                return
            helper(root.left,list1)
            helper(root.right,list1)
        list1=[]
        list2=[]
        helper(root1,list1)
        helper(root2,list2)
        if list1==list2:
            return True
        else:
            return False
