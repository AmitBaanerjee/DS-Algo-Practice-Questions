
# coding: utf-8

# In[7]:


class Queue(object):
    def __init__(self):
        self.items=[]
    def push(self,value):
        self.items.append(value)
    def isEmpty(self):
        return len(self.items)==0
    def pop(self):
        if not self.isEmpty():
            return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)
    def printElements(self):
        if not self.isEmpty():
            for i in self.items:
                print(i,end=" ")
        else:
            print("No elements to print!")
q=Queue()
q.push(1)
q.push(2)
q.push(3)
q.isEmpty()
q.pop()
q.peek()
q.size()
q.printElements()

