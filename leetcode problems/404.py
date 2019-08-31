# 404. Sum of Left Leaves
#
# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
            if root==None:
                return 0
            q=deque()
            q.append(root)
            nodes=0
            while q:
                current=q.popleft()
                if current.left and current.left.left==None and current.left.right==None:
                    nodes+=(current.left.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            return nodes
