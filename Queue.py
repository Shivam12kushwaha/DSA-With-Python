class Queue:
    def __init__(self):
        self.lst = []

    def isEmpty(self):
        return len(self.lst) == 0
    
    def insert(self, value):
        self.lst.append(value)

    def delete(self):
        if self.isEmpty():
            print('Queue is Empty')
        else:
            return self.lst.pop(0)
        

# Examples
obj = Queue()
obj.insert(10)
obj.insert(20)
obj.insert(30)
print(obj.delete())
print(obj.delete())
print(obj.delete())
print(obj.delete())
print(obj.delete())