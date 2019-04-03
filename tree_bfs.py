
# coding: utf-8

# In[60]:


class Queue(object):
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()
    def peek(self):
        if not self.isEmpty():
            return self.items[-1].value
    def isEmpty(self):
        if len(self.items)==0:
            return True
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)
    
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    
    def preorder_print(self,head,display):
        if head:
            display+=(str(head.value)+"->")
            display=self.preorder_print(head.left,display)
            display=self.preorder_print(head.right,display)
        return display
    def inorder_print(self,head,display):
        if head:
            display=self.inorder_print(head.left,display)
            display+=(str(head.value)+"->")
            display=self.inorder_print(head.right,display)
        return display
    def postorder_print(self,head,display):
        if head:
            display=self.postorder_print(head.left,display)
            display=self.postorder_print(head.right,display)
            display+=(str(head.value)+"->")
        return display
    def bfs(self,head):
        if head ==None:
            return 0
        display=""
        q=Queue()
        q.enqueue(head)
            
        while len(q)>0:
            display+=str(q.peek())+"->"
            node=q.dequeue()
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
        return display
            
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print("preorder",tree.preorder_print(tree.root,""))
print("inorder",tree.inorder_print(tree.root,""))
print("postorder",tree.postorder_print(tree.root,""))
print("bfs",tree.bfs(tree.root))


#             1
#           /   \
#          2     3
#         /\    / \
#        4  5   6  7
      


# In[58]:




