# 589. N-ary Tree Preorder Traversal
#
# Given an n-ary tree, return the preorder traversal of its nodes' values.
#
# For example, given a 3-ary tree:
#
#              1
#           /  |  \
#          3   2   4
#         / \
#        5   6

# Return its preorder traversal as: [1,3,5,6,2,4].
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root==None:
            return []
        result=[]
        stack=deque()
        stack.append(root)
        while stack:
            node=stack.pop()
            result.append(node.val)
            for c in node.children[::-1]:
                stack.append(c)
        return result
