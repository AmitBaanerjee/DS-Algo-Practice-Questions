111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def helper(root,count,store):
            if root==None:
                return
            if root.left==None and root.right==None:
                store.append(count)
                return
            helper(root.left,count+1,store)
            helper(root.right,count+1,store)

        if root==None:
            return 0
        store=[]
        helper(root,1,store)
        return min(store)
