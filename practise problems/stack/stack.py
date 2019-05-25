
# coding: utf-8

# In[4]:


class Stack(object):
    def __init__(self):
        self.items=[]
    def push(self,value):
        self.items.append(value)
    def pop(self):
        if not isEmpty():
            return self.items.pop()
        else:
            return "No Elements"
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items)==0
    def printElements(self):
        if self.isEmpty():
            return None
        else:
            for i in self.items:
                print(i)
        
        

s=Stack()
s.push(2)
s.push(3)
s.peek()
s.pop()
s.printElements()
s.push(90)
s.printElements()


# In[3]:




