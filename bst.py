
# coding: utf-8

# In[18]:


class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
class Bst(object):
    def __init__(self):
        self.root=None
    def insert(self,item):
        self.insert_helper(self.root,item)
    def insert_helper(self,current,item):
        if current is None:
            self.root=Node(item)
            return
        if current.value<item:
            if current.right:
                self.insert_helper(current.right,item)
            else:
                current.right=Node(item)
        else:
            if current.left:
                self.insert_helper(current.left,item)
            else:
                current.left=Node(item)
    def search(self,item):
        if self.root:
            returnvalue=self.search_helper(self.root,item)
            if returnvalue:
                return True
            else:
                return False
        else :
            return False
        self.search_helper(self.root,item)
    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
b=Bst()
b.insert(2)
b.insert(1)
b.insert(6)
b.insert(5)
print(b.search(2))

