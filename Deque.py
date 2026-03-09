class Deque:
    def __init__(self):
        self.lst = []

    # Fnction to check if deque is empty.
    def isEmpty(self):
        return len(self.lst) == 0
    
    # Function to insert at the end
    def insertAtEnd(self, value):
        self.lst.append(value)

    # Function to insert at the beginning
    def insertAtBegin(self, value):
        self.lst.insert(0, value)

    #Function to delete from the beginning
    def deleteAtBegin(self):
        if self.isEmpty():
            print('Deque is Empty')
        else:
            return self.lst.pop(0)

    # Function to delete from the end
    def deleteAtEnd(self):
        if self.isEmpty():
            print('Deque is Empty')
        else:
            return self.lst.pop()


# Examples
dq = Deque()
dq.insertAtBegin(10)
dq.insertAtEnd(20)
dq.insertAtEnd(30)
dq.insertAtBegin(50)
print(dq.deleteAtBegin())
print(dq.deleteAtEnd())
print(dq.deleteAtEnd())
print(dq.deleteAtBegin()) 
print(dq.deleteAtBegin()) 
print(dq.deleteAtBegin())        