
# coding: utf-8

# In[ ]:


#Program to check if two trees are the same

#TREE 1
#      5
#    /  \
#   4    9
#  / \  / \
# 3  6 8  10        

#TREE2
#      5
#    /  \
#   4    9
#  / \  / \
# 3  6 8  10


# In[15]:


class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class Tree:
    def __init__(self,value):
        self.root=Node(value)
def SameTreeCheck(head1,head2):
    if head1 is None and head2 is None:
        return True
    if head1 and head2:
        return (head1.value==head2.value and SameTreeCheck(head1.left,head2.left) and SameTreeCheck(head1.right,head2.right))
    return False
t=Tree(5)
t.root.left=Node(4)
t.root.right=Node(9)
t.root.left.left=Node(3)
t.root.left.right=Node(6)
t.root.right.left=Node(8)
t.root.right.right=Node(10)

t2=Tree(5)
t2.root.left=Node(4)
t2.root.right=Node(10)
t2.root.left.left=Node(3)
t2.root.left.right=Node(6)
t2.root.right.left=Node(8)
t2.root.right.right=Node(10)

print(SameTreeCheck(t.root,t2.root))

