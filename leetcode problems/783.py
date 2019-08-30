# 783. Minimum Distance Between BST Nodes
#
# Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.
#
# Example :
#
# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.
#
# The given tree [4,2,6,1,3,null,null] is represented by the following diagram:
#
#           4
#         /   \
#       2      6
#      / \
#     1   3
#
# while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q=deque()
        q.append(root)
        values=[]
        diff=[]
        while(q):
            current=q.popleft()
            values.append(current.val)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        values.sort()
        for i in range(0,len(values)-1):
            diff.append(abs(values[i]-values[i+1]))
        return min(diff)
