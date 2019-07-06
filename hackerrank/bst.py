#given a tree find the number of edges connecting root node and the furthest child node 


class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeightNodes(self,root):
        if root==None:
            return 0
        leftheight=self.getHeightNodes(root.left)
        rightheight=self.getHeightNodes(root.right)
        return 1+max(leftheight,rightheight)

    def getHeight(self,root):
        edgeheight=self.getHeightNodes(root)-1
        return edgeheight

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
