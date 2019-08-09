# 637. Average of Levels in Binary Tree
#
# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
#
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# Note:
#
# The range of node's value is in the range of 32-bit signed integer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result=[]
        queue=deque()
        queue.append(root)
        while queue:
            tempqueue=[]
            while len(queue)!=0:
                tempqueue.append(queue.pop())
            sum=0
            for i in tempqueue:
                sum+=i.val
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
            result.append(sum/len(tempqueue))
        return result
