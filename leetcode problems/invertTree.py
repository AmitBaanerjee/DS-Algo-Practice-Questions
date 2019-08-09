# 226. Invert Binary Tree
#
# Invert a binary tree.
#
# Example:
#
# Input:
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q=deque()
        if root==None:
            return None
        q.append(root)
        while q:
            current = q.popleft()
            current.left,current.right=current.right,current.left
            if current.left!=None:
                q.append(current.left)
            if current.right!=None:
                q.append(current.right)
        return root
