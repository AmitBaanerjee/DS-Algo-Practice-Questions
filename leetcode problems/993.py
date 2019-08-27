993. Cousins in Binary Tree

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:

        1
      /   \
     2     3
    /
   4

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
        1
     /     \
    2       3
     \        \
      4         5

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:

        1
     /     \
    2       3
     \
      4


Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def check_cousins(self,d,x,y):
        if x in d and y in d:
            if d[x]!=d[y]:
                return True
            else:
                return False
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q=[root]
        d=defaultdict(int)
        while q:
            temp=[]
            while(len(q)!=0):
                current=q.pop()
                if current.left:
                    temp.append(current.left)
                    d[current.left.val]=current.val
                if current.right:
                    temp.append(current.right)
                    d[current.right.val]=current.val
            flag=self.check_cousins(d,x,y)
            if flag==True:
                return True
            else:
                q=temp
                d.clear()
        return False
