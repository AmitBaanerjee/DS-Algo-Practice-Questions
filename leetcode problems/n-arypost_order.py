# 590. N-ary Tree Postorder Traversal
#
# Given an n-ary tree, return the postorder traversal of its nodes' values.
#
# For example, given a 3-ary tree:
#
#              1
#           /  |  \
#          3   2   4
#         / \
#        5   6
#
# Return its postorder traversal as: [5,6,3,2,4,1].
#
# Note:
#
# Recursive solution is trivial, could you do it iteratively?

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack,queue=deque(),deque()
        stack.append(root)
        if root ==None:
            return []
        while(stack):
            node=stack.pop()
            queue.appendleft(node.val)
            for i in node.children:
                stack.append(i)
        return queue
