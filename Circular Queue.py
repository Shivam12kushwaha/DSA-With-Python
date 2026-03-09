class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.lst = [None]*size
        self.front = self.rear = -1


    # Function to insert the element in the queue
    def enqueue(self, val):
        if (self.rear+1)%self.size == self.front:
            print('Queue is Full')

        elif self.front == -1:
            self.front = self.rear = 0
            self.lst[self.rear] = val

        else: 
            self.rear = (self.rear+1) % self.size
            self.lst[self.rear] = val

    # Function to delete the elements

    def dequeue(self):
        if self.front == -1:
            print('Queue is Empty')

        elif self.front == self.rear:
            print(self.lst[self.front])
            self.front = self.rear = -1

        else:
            print(self.lst[self.front])
            self.front = (self.front+1)%self.size


# Examples
cq = CircularQueue(4)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.dequeue()
cq.enqueue(50)