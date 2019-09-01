# 654. Maximum Binary Tree
#
# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
#
# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.
#
# Example 1:
#
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
#
#       6
#     /   \
#    3     5
#     \    /
#      2  0
#        \
#         1

  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, x):
  #         self.val = x
  #         self.left = None
  #         self.right = None

  class Solution:
      def find_max(self,low,high,nums):
          temp=low
          for i in range(low,high):
              if nums[i]>nums[temp]:
                  temp=i
          return temp
      def construct(self,low,high,nums):
          if low==high:
              return
          max_index=self.find_max(low,high,nums)
          root=TreeNode(nums[max_index])
          root.left=self.construct(low,max_index,nums)
          root.right=self.construct(max_index+1,high,nums);
          return root

      def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
          return self.construct(0,len(nums),nums)
