# 107. Binary Tree Level Order Traversal II
#
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        q=deque()
        q.append(root)
        result=deque()
        while (q):
            temp_q=[]
            temp_result=[]
            while len(q)!=0:
                temp_q.append(q.popleft())
            for i in temp_q:
                if i.left:
                    q.append(i.left)
                if i.right:
                    q.append(i.right)
                temp_result.append(i.val)
            result.appendleft(temp_result)
        return result
