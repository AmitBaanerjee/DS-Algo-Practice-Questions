#
# 429. N-ary Tree Level Order Traversal
#
# Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# # For example, given a 3-ary tree:
# #
# #              1
# #           /  |  \
# #          3   2   4
# #         / \
# #        5   6
#
# We should return its level order traversal:
#
# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result=[]
        if root==None:
            return []
        queue=[root]
        while queue:
            level_nodes=[]
            for i in queue:
                level_nodes.append(i.val)
            result.append(level_nodes)
            tmp=[]
            for i in queue:
                if i.children:
                    for j in i.children:
                        tmp.append(j)
                queue=tmp
        return result
