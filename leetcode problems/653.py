653. Two Sum IV - Input is a BST

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True


Example 2:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    ##OPTIMAL SOLUTION
    def find(self,root,k,s):
            if root==None:
                return False
            if (k-root.val) in s:
                return True
            s.add(root.val)
            return self.find(root.left,k,s) or self.find(root.right,k,s)

    # def num_check(self,numbers,k):
    #     for i in range(len(numbers)):
    #         for j in range(i+1,len(numbers)):
    #             if numbers[i]+numbers[j]==k:
    #                 return True
    #     return False

    def findTarget(self, root: TreeNode, k: int) -> bool:
        # q=deque()
        # q.append(root)
        # numbers=[]
        # while(q):
        #     current=q.popleft()
        #     numbers.append(current.val)
        #     if current.left:
        #         q.append(current.left)
        #     if current.right:
        #         q.append(current.right)
        # return self.num_check(numbers,k)

        ##OPTIMAL SOLUTION

        s=set()
        return self.find(root,k,s)



            
