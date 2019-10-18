297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):

        def s(root,elements):
            if root==None:
                elements.append("None")
                return
            elements.append(str(root.val))
            s(root.left,elements)
            s(root.right,elements)

        elements=[]
        s(root,elements)
        return ",".join(elements)

    def deserialize(self, data):

        def d(data):
            if len(data)==d.idx or data[d.idx]=="None" :
                d.idx+=1
                return None
            root=TreeNode(data[d.idx])
            d.idx+=1
            root.left=d(data)
            root.right=d(data)
            return root
        d.idx=0
        data_list=data.split(',')
        return d(data_list)
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
