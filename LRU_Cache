class LRUCache:

    def __init__(self, capacity: int):
        self.d= collections.OrderedDict()
        self.remaining=capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        temp=self.d.pop(key)
        self.d[key]=temp
        return self.d[key]

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.pop(key)
        else:
            if self.remaining>0:
                self.remaining-=1
            else:
                self.d.popitem(last=False)
        self.d[key]=value
