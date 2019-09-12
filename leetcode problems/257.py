257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    result=[]
    def calc(self,root,stack):
        if root==None:
            return
        stack.append(root)
        if root.left==None and root.right==None:
            self.result.append('->'.join([str(i.val) for i in stack]))
        self.calc(root.left,stack)
        self.calc(root.right,stack)
        stack.pop()

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        stack=[]
        self.result=[]
        self.calc(root,stack)
        return self.result
