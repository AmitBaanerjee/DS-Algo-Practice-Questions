
# coding: utf-8

# In[9]:


class Node(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Stack(object):
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not len(self.items)==0:
            return self.items.pop()
    def size(self):
        return len(self.items)
    def __len__(self):
        return self.size()
    
class Tree(object):
    def __init__(self,root):
        self.root=Node(root)
    def size(self,start):
        if start==None:
            return 0
        s=Stack()
        s.push(start)
        counter=1
        while len(s)>0:
            node=s.pop()
            if node.left:
                s.push(node.left)
                counter+=1
            if node.right:
                s.push(node.right)
                counter+=1
        return counter
                
    def height(self,start):
        if start==None:
            return 0
        leftheight=self.height(start.left)
        rightheight=self.height(start.right)
        return 1+max(leftheight,rightheight)
        
t=Tree(1)
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.left.right=Node(5)
t.root.right.left=Node(6)
t.root.right.right=Node(7)
print("size of tree is :",t.size(t.root))
print("height of tree is :",t.height(t.root))

